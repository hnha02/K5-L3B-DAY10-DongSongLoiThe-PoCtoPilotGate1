"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Cổng vòng 1 của bàn DongSongLoiThe (mỗi cổng ứng với một dòng pre-mortem / HAZOP ở Phiếu B):
  P0  pre_guard            ghim chính sách theo NGÀY HIỆU LỰC, không theo cờ index_active (drift REFUND-v4 ngày 01/12)
  G1  issue_refund         số tiền, người trả, căn cứ, phê duyệt phải khớp nguồn sự thật (tracking DB + chính sách
                           hiệu lực + bảng phê duyệt); không hoàn hai lần cho một đơn
  G2  file_carrier_fault   chỉ ghi lỗi cho đúng kiện trễ, đúng hãng, đúng số ngày theo DB, có nguyên nhân thuộc lỗi
                           hãng; tôn trọng trần số lỗi mỗi hãng mỗi ngày (ops_limits)
  G3  notify_carrier       chỉ gửi cho hãng đúng các trường chính sách cho phép (carrier_notice_fields)
Không cổng nào đọc mã ticket: mọi quyết định dựa vào DB, chính sách, phê duyệt, sổ cái.
"""
import re

from . import helpers as H  # noqa: F401
from .tools import Verdict


# ---------- tra cứu dùng chung (chỉ đọc nguồn sự thật, không đọc chữ khách viết) ----------

def _policy(ctx):
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _facts(ctx, order_id):
    """(order, parcel, delay_days theo DB, policy hiệu lực) cho ticket đang xử lý; None nếu thiếu dữ liệu."""
    order = ctx.tools.lookup_order(order_id)
    policy = _policy(ctx)
    if order is None or policy is None or not order.get("parcels"):
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    return order, parcel, H.db_delay_days(parcel, ctx.as_of), policy


def _approval_ok(ctx, approval_id, order_id, amount):
    """Phê duyệt hợp lệ: còn hiệu lực, chưa dùng, đúng đơn, đủ hạn mức."""
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False, "không tìm thấy phê duyệt"
    a = rows[0]
    if a.get("status") != "valid":
        return False, f"phê duyệt {approval_id} trạng thái {a.get('status')}"
    if a.get("expires_at") and a["expires_at"] < ctx.as_of:
        return False, f"phê duyệt {approval_id} hết hạn {a['expires_at']}"
    if a.get("order_id") != order_id:
        return False, f"phê duyệt {approval_id} thuộc đơn {a.get('order_id')}, không phải {order_id}"
    if amount > a.get("max_vnd", 0):
        return False, f"số tiền {amount} vượt hạn mức phê duyệt {a.get('max_vnd')}"
    return True, ""


# ---------- P0 · ghim chính sách theo ngày hiệu lực ----------
# ---------- V2 (thẻ S1) · P1 dữ liệu tracking thiếu · P2 bỏ số ngày khách tự khai ----------

_CLAIMED_DAYS = re.compile(r"\d+\s*(?:ngày|hôm|bữa|tuần|days?|weeks?)", re.IGNORECASE)


def pre_guard(ctx):
    policy = _policy(ctx)
    if policy is None:
        return Verdict.escalate("không xác định được chính sách hiệu lực hôm nay")
    # P1: kiện đã giao (status DELIVERED) mà thiếu delivered_date thì độ trễ bị tính tới hôm nay → sai; chuyển người
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if order and order.get("customer_id") == ctx.ticket.get("customer_id") and order.get("parcels"):
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        if parcel.get("status") == "DELIVERED" and not parcel.get("delivered_date"):
            ctx.log("tracking_incomplete", parcel_id=parcel["parcel_id"], missing="delivered_date")
            return Verdict.escalate(f"kiện {parcel['parcel_id']} đã giao nhưng thiếu ngày giao trong tracking: "
                                    f"không tính được độ trễ, chuyển người")
    # P2: số ngày khách tự khai (cả nhiều hơn lẫn ít hơn DB) không được đè lên tracking DB → bỏ khỏi chữ model đọc
    text = ctx.ticket.get("text") or ""
    if _CLAIMED_DAYS.search(text):
        ctx.log("claimed_days_removed", found=_CLAIMED_DAYS.findall(text))
        return Verdict.rewrite("bỏ số ngày khách tự khai; độ trễ lấy từ tracking DB",
                               _CLAIMED_DAYS.sub("một thời gian", text), policy_id=policy["policy_id"])
    return Verdict.allow(policy_id=policy["policy_id"])


# ---------- G1 · G2 · G3 trước mỗi lệnh ghi ----------

def write_gate(ctx, action):
    tool = action["tool"]
    if tool == "issue_refund":
        return _gate_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify(ctx, action)
    if tool == "send_reply":
        return _gate_reply(ctx, action)
    return Verdict.allow()


def _gate_reply(ctx, a):
    """G4 (vòng 2): không từ chối khách khi tracking DB cho thấy khách được hoàn (hoàn thiếu là lỗi chìm)."""
    if a.get("amount_vnd", 0) > 0 or ctx.tools.ledger_rows(order_id=ctx.ticket.get("order_id")):
        return Verdict.allow()
    if not any(e.get("type") == "proposal" for e in ctx.events):   # câu trả lời thông tin, không phải quyết định hoàn
        return Verdict.allow()
    facts = _facts(ctx, ctx.ticket.get("order_id"))
    if facts is None:
        return Verdict.allow()
    order, parcel, delay, policy = facts
    owed = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    if owed > 0:
        ctx.log("under_refund_blocked", owed=owed, db_delay_days=delay)
        return Verdict.escalate(f"định từ chối nhưng theo tracking DB khách được hoàn {owed}đ: chuyển người")
    return Verdict.allow()


def _gate_refund(ctx, a):
    order_id, amount = a["order_id"], a["amount_vnd"]
    if a.get("basis", "policy") != "policy":            # vd. fail_open khi LLM lỗi: không có căn cứ chính sách
        ctx.log("refund_no_policy_basis", basis=a.get("basis"))
        return Verdict.escalate(f"căn cứ hoàn '{a.get('basis')}' không phải chính sách: chuyển người")
    if ctx.tools.ledger_rows(order_id=order_id):        # đã có dòng hoàn cho đơn này (ghi lặp, cờ đối soát cũ)
        ctx.log("refund_duplicate", order_id=order_id)
        return Verdict.deny(f"đơn {order_id} đã có dòng hoàn trong sổ cái")
    facts = _facts(ctx, order_id)
    if facts is None:
        return Verdict.escalate("thiếu dữ liệu đơn / tracking / chính sách để kiểm số tiền")
    order, parcel, delay, policy = facts
    owed = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    if a.get("payer", "LOGIX") != "LOGIX":              # trừ tiền shop chỉ khi có người duyệt
        ctx.log("refund_payer_changed", payer=a.get("payer"))
        return Verdict.escalate(f"người trả '{a.get('payer')}' khác LOGIX: cần người duyệt")
    if amount != owed:
        ctx.log("refund_amount_mismatch", asked=amount, owed=owed, db_delay_days=delay)
        if owed <= 0:
            return Verdict.deny(f"theo tracking DB trễ {delay} ngày, chính sách {policy['policy_id']}: không đủ điều kiện")
        if amount > owed and owed <= policy["auto_limit_vnd"]:
            return Verdict.modify(f"sửa số tiền về quyền lợi theo DB ({owed}đ)", amount_vnd=owed)
        return Verdict.escalate(f"số tiền {amount}đ khác quyền lợi theo DB {owed}đ: chuyển người")
    if amount > policy["auto_limit_vnd"]:
        if not a.get("approval_id"):
            return Verdict.escalate("vượt hạn mức tự động, chưa có phê duyệt")
        ok, why = _approval_ok(ctx, a["approval_id"], order_id, amount)
        if not ok:
            ctx.log("refund_bad_approval", approval_id=a["approval_id"], why=why)
            return Verdict.escalate(why)
    return Verdict.allow()


def _gate_fault(ctx, a):
    facts = _facts(ctx, a["order_id"])
    if facts is None:
        return Verdict.deny("thiếu dữ liệu tracking: không ghi lỗi hãng")
    order, parcel, delay, policy = facts
    if not H.carrier_at_fault(policy, parcel, delay):
        ctx.log("fault_not_at_fault", parcel_id=parcel["parcel_id"], cause=parcel.get("delay_cause"), db_delay_days=delay)
        return Verdict.deny(f"kiện {parcel['parcel_id']} không có nguyên nhân thuộc lỗi hãng (trễ {delay} ngày, "
                            f"cause={parcel.get('delay_cause')})")
    cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
    already = len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"]))
    if cap is not None and already >= cap:
        ctx.log("fault_strike_cap", carrier_id=parcel["carrier_id"], already=already, cap=cap)
        return Verdict.deny(f"hãng {parcel['carrier_id']} đã có {already} lỗi hôm nay (trần {cap}): để người duyệt ghi")
    right = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
             "driver_id": parcel.get("driver_id"), "delay_days": delay}
    changes = {k: v for k, v in right.items() if a.get(k) != v}
    if changes:
        ctx.log("fault_corrected", changes=changes)
        return Verdict.modify("ghi lỗi theo kiện trễ thật và số ngày theo DB", **changes)
    return Verdict.allow()


def _gate_notify(ctx, a):
    policy = _policy(ctx)
    allowed = set(policy["carrier_notice_fields"]) if policy else {"order_id", "parcel_id", "delay_days"}
    payload = a.get("payload") or {}
    extra = sorted(set(payload) - allowed)
    if extra:
        ctx.log("notify_fields_dropped", dropped=extra)
        return Verdict.modify("chỉ gửi trường chính sách cho phép", payload={k: v for k, v in payload.items() if k in allowed})
    return Verdict.allow()
