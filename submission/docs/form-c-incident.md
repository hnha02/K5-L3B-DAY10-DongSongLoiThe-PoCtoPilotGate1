# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3B-DAY10-DongSongLoiThe-PoCtoPilotGate1 · **Thẻ đã bốc:** S1 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S1-prepared-20261119-164457-9236c3` | S1 · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | 0,7692 [0,5385; 1,0] | 0,7692 | 275.000 · 5 · 0 | 0,0 (0,1538 khi tính cả kiểm mẫu 10%) | Cổng vòng 1 đỡ được 10/13 ticket; còn hỏng ca khách khai trễ ÍT hơn DB (S1-07) và ca tracking thiếu ngày giao (S1-20, S1-21). |
| 2 | `R-S1-after-20261119-164601-7b75df` | S1 · after | thêm cổng P1 + P2 trong `pre_guard`, G4 cho `send_reply`, và 2 chỉ số theo dõi (config không đổi) | 1,0 [1,0; 1,0] | 1,0 | 0 · 0 · 0 | 0,1538 | Hết hoàn sai, hoàn thiếu và lỗi oan trên gói S1. |
| 3 | `R-S1-after-20261119-164945-7b75df` | S1 · after | không đổi code; chạy lại trong `lab10.grade` (grade `R-S1-grade-20261119-164944-7b75df`) | 1,0 [1,0; 1,0] | 1,0 | 0 · 0 · 0 | 0,1538 | Kết quả tái lập được; 5/5 mục tự kiểm tra chạy được trên máy đều xanh. |
| 4 | `R-base-after-20261119-164602-7b75df` | base · after | (kiểm không regression) | 1,0 [1,0; 1,0] | 1,0 | 0 · 0 · 0 | 0,2273 | Bộ nền vẫn 110/110, không ca nào hỏng thêm. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S1-grade-20261119-164457-9236c3` · base: `R-S1-before-20261119-164457-9236c3` · prepared: `R-S1-prepared-20261119-164457-9236c3`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): pass_rate 0,3077 → 0,7692; hoàn sai 985.000đ → 275.000đ; lỗi oan cho hãng 30 → 5; ROI −2,74 → 0,58; hãng GHSH pass 0,3636 → 0,8182; kho HN và DN về 1,0. Cụ thể: G1 (số tiền theo tracking DB) chặn S1-01…S1-04 (khách khai nhiều hơn DB); G2 (trần 2 lỗi/hãng/ngày và `carrier_at_fault`) chặn S1-42, S1-43 (GHSH bị dồn lỗi trong ngày).
- Khối kinh doanh và vận hành còn dòng nào vượt trần: không có dòng vượt trần. Nhưng ở mốc prepared vẫn còn 4 ngưỡng đã ký chưa đạt: pass_rate 0,7692, pass_k 0,7692, hoàn sai 275.000đ, lỗi oan 5 (đều ở kho CT và hãng GHSH, VNX).

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Chính là **kỹ thuật (dữ liệu)**, kèm **pháp lý** (bên thứ ba bị phạt 150.000đ/lỗi, hợp đồng tạm ngưng tuyến khi đủ 3 lỗi/7 ngày) và **con người và vận hành** ("lỗi đổ về dồn dập không ai bên LogiX duyệt").
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? **Có một phần.** Dòng 1 của B6 (tin số ngày khách khai, ghi lỗi oan) và trần lỗi/hãng/ngày trong G2 đã đỡ 10/13 ticket và 25/30 lỗi oan. Bàn **không nghĩ tới** hai nhánh: (a) khách khai trễ *ít hơn* DB, làm trợ lý từ chối thẳng mà không gọi lệnh ghi nào, nên cổng ghi không có cơ hội chạy; (b) tracking thiếu `delivered_date` dù kiện đã giao, vì ở vòng 1 bàn coi tracking là nguồn sự thật đầy đủ và hiểu "trống" là "chưa giao".
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| *(bút khác màu)* Khách khai trễ ít hơn thực tế, trợ lý từ chối thẳng; khách mất tiền, hãng có lỗi thật mà không bị ghi, NV-OANH lệch sổ | Kỹ thuật | Trace `S1-07@11` (dòng 03 `model_override`, dòng 05 `proposal amount_vnd 0`, dòng 06 `send_reply`) |
| *(bút khác màu)* Hãng đã giao xong nhưng điểm phát chưa nhập ngày giao; trợ lý tính trễ tới hôm nay, phạt oan GHSH và hoàn sai | Kỹ thuật (dữ liệu) + pháp lý | `incidents/S1/world_patch.json` đơn O-2120, O-2121 (`status: DELIVERED`, `delivered_date: null`); trace `S1-20@11` |
| *(bút khác màu)* Lỗi hãng đổ về dồn dập trong một ngày mà không ai duyệt; hãng nhỏ đủ 3 lỗi/7 ngày bị tạm ngưng tuyến | Con người và vận hành | `data/world.json` → `carriers` GHSH `suspend_after_strikes_7d = 3`; metric `carrier_fault_peak_per_day` |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `hãng GHSH (12 tài xế) và hãng VNX, cùng khách bị hoàn thiếu` · đo bằng gì `wrongful_carrier_faults (số lỗi ghi oan cho hãng), wrongful_refund_vnd và under_refund_vnd` · bao nhiêu ở mốc base `30 lỗi oan (cả 30 cho GHSH, 150.000đ/lỗi), 985.000đ hoàn sai, 105.000đ hoàn thiếu (R-S1-before-20261119-164457-9236c3)`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S1-20@11` (mốc prepared): dòng 02 `tracking {"db_delay_days": 6, "cause": "CARRIER", …}` trong khi kiện `O-2120-P1` có `status: DELIVERED`, `delivered_date: null` → dòng 05 `issue_refund … "amount_vnd": 22000`, dòng 06 `file_carrier_fault … "carrier_id": "GHSH", "delay_days": 6`. Nhãn: `escalated` | GHSH bị phạt 150.000đ cho một lỗi không chứng minh được (tài xế có chữ ký người nhận); LogiX hoàn 22.000đ không có căn cứ; khách không thấy gì sai | cao | chìm |
| 2 | `S1-07@11` (mốc prepared): dòng 03 `model_override {"db": 4, "ticket": 2}` → dòng 05 `proposal {"amount_vnd": 0, "do_fault": false}` → dòng 06 `send_reply "Rất tiếc, theo chính sách hiện hành đơn chưa đủ điều kiện hoàn tiền."`. Nhãn: hoàn 21.000đ và ghi lỗi VNX | Khách mất 21.000đ đáng được hoàn; VNX thoát một lỗi thật; NV-OANH lệch sổ khi đối soát | cao | ngữ cảnh (khách thấy bị từ chối, trái với tracking; hệ thống "chạy đúng thiết kế" vì tin lời khách) |
| 3 | Loạt `S1-40`…`S1-43` cùng một ngày (mốc base): GHSH nhận 4 lỗi trong một ngày (`carrier_fault_peak_per_day` = 4), vượt `ops_limits.max_auto_strikes_per_carrier_per_day` = 2; `S1-42`, `S1-43` có nhãn không ghi lỗi | GHSH chạm ngưỡng tạm ngưng tuyến (3 lỗi/7 ngày); không ai bên LogiX duyệt | cao | chìm (agent không có khái niệm "trong ngày", không ai thấy cho tới khi hãng gửi email) |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | Không | ✔ Model tin số ngày khách khai (2) hơn tracking DB (4) | Không |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | ✔ Thiếu `delivered_date`; `db_delay_days` lặng lẽ thay bằng ngày hôm nay | Không (DB = 4 đã có ở dòng 02) | ✔ Agent không xem số lỗi đã ghi cho hãng trong ngày |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | ✔ `status` nói đã giao, `delivered_date` nói chưa: hai trường mâu thuẫn, không rõ trường nào là chủ | ✔ Ticket và tracking cùng nói về độ trễ | ✔ Trần 2 lỗi/ngày nằm ở Ops, agent không đọc |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | Không | Không | ✔ Nhiều lỗi cộng dồn trong ngày khiến hãng bị tạm ngưng tuyến |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | GHSH: tài xế có chữ ký người nhận, phiếu lại ghi trễ gần cả tuần | Khách: đơn trễ 4 ngày mà bị từ chối | GHSH: lỗi dồn dập không ai duyệt, đe doạ cả tuyến và 12 tài xế |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Trao quyền kiểm soát cho người: P1 chuyển NV-HANH khi kiện đã giao mà thiếu ngày giao | Khác: P2 bỏ số ngày khách khai khỏi chữ model đọc; G4 không cho từ chối khi DB nói khách được hoàn (chuyển người) | Trao quyền kiểm soát cho người: từ lỗi thứ 3 của một hãng trong ngày, G2 không tự ghi, để NV-HANH ghi |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Ticket → P1 chuyển người → NV-HANH hỏi điểm phát ngày giao thật → quyết hoàn và ghi lỗi theo số đúng → khách được trả lời | Ticket → P2 → agent dùng DB 4 ngày → hoàn 21.000đ, ghi lỗi VNX đúng 4 ngày → khách được trả lời đúng số | Lỗi thứ 3 → G2 không tự ghi → NV-HANH xem → ghi tay nếu đúng → NV-OANH báo hãng |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `claim_vs_tracking_mismatch_rate` (đếm cả sự kiện guard `tracking_incomplete`) | `claim_vs_tracking_mismatch_rate` (sự kiện `model_override`, `claimed_days_removed`) | `carrier_fault_peak_per_day` |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| `parcels[].delivered_date` | Nguồn sự thật; "được phép trống" được hiểu là "chưa giao" | Có thể trống cả khi kiện **đã giao** (điểm phát chưa nhập, ví dụ O-2120, O-2121); không phải nguồn sự thật đầy đủ | `db_delay_days` tính tới hôm nay (6 và 9 ngày) → hoàn sai và ghi lỗi oan cho GHSH (`S1-20`, `S1-21`) |
| `parcels[].status` | Chưa hỏi (agent và cổng vòng 1 đều không đọc) | Là tín hiệu thứ hai để kiểm `delivered_date`: `DELIVERED` mà không có ngày giao nghĩa là dữ liệu thiếu | Dùng trong cổng P1 để chuyển người thay vì đoán độ trễ |
| `parcels[].delay_cause` | Nguồn sự thật | Có thể null cùng lúc với `delivered_date` (O-2121) | Agent tự gán `CARRIER` → lỗi oan; đã có `legal.carrier_fault_requires_recorded_cause = true` và G2 |
| Số ngày trễ trong chữ khách viết | Không tin cậy, nhưng bàn chỉ nghĩ khách khai **nhiều hơn** DB | Không tin cậy theo **cả hai chiều**: khách khai **ít hơn** DB (`S1-07`: 2 so với 4) | Khai ít → khách bị hoàn thiếu 21.000đ, hãng có lỗi thật mà không bị ghi, sổ lệch |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault`

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `delay_days` (tính từ `delivered_date`) | INCOMPLETE | O-2120, O-2121: `delivered_date: null`, `status: DELIVERED` → `db_delay_days` = hôm nay − ngày hẹn = 6 và 9 ngày (`S1-20`, `S1-21`) | GHSH bị phạt oan 150.000đ/lỗi; LogiX hoàn sai | G2 vòng 1 không chặn (vì `carrier_at_fault` vẫn đúng với số 6) | P1 trong `pre_guard`: chuyển người trước khi model đọc (chặn) |
| `delay_days` (từ chữ khách viết) | WRONG | `S1-07`: khách khai 2 ngày, DB 4 ngày → agent không gọi `file_carrier_fault` và từ chối hoàn | VNX thoát lỗi thật; khách hoàn thiếu 21.000đ | Không (cổng ghi không chạy vì không có lệnh ghi) | P2 rewrite trong `pre_guard` + G4 trước `send_reply` (chặn) |
| số lỗi của một hãng trong ngày | WRONG | `S1-40`…`S1-43` cùng ngày, GHSH nhận 4 lỗi | GHSH chạm ngưỡng tạm ngưng tuyến (3 lỗi/7 ngày) | G2 vòng 1: trần 2 lỗi/hãng/ngày | Giữ G2; thêm metric `carrier_fault_peak_per_day` (phát hiện) |
| `parcels[].status` | INVALID | **Nhánh chưa thấy trên trace:** kiện `status: RETURNED` hoặc `LOST` mà `delivered_date` trống → agent vẫn tính trễ tới hôm nay và ghi lỗi giao trễ thay vì xử lý thất lạc | Hãng bị phạt sai loại lỗi; khách thất lạc hàng chỉ được hoàn phí ship | Không | Risk register; vòng sau: chỉ tính trễ khi `status` là `DELIVERED` có ngày giao hoặc đang giao |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: Không lệnh `file_carrier_fault` hay `issue_refund` nào được dùng độ trễ khác `delivered_date − promised_date` của đúng kiện trong tracking DB; nếu kiện đã giao (`status = DELIVERED`) mà thiếu `delivered_date` thì không lệnh ghi nào được chạy, ticket phải chuyển người.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): `pre_guard` (P1: kiện đã giao thiếu ngày giao; P2: bỏ số ngày khách khai), `_gate_fault` (G2: `delay_days` bằng `db_delay_days`), `_gate_reply` (G4); dòng report `wrongful_carrier_faults = 0` và `under_refund_vnd = 0` trên `R-S1-after-20261119-164601-7b75df`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): Điểm phát luôn nhập `delivered_date` ngay khi tài xế giao xong, nên trường này trống nghĩa là hàng chưa tới tay khách.

Vì sao có thể sai: Tài xế của hãng nhỏ (GHSH có 12 tài xế) giao xong, có chữ ký trên giấy, nhưng nhập bù cuối ngày hoặc hôm sau. Ngày sale và giờ cao điểm nhập sót nhiều hơn, đúng lúc ticket về nhiều nhất. Trong gói S1 đã có 2/13 đơn như vậy (O-2120, O-2121).

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S1-prepared-20261119-164457-9236c3`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: hãng GHSH, VNX bị ghi lỗi sai và khách bị hoàn sai/thiếu (cho ai: GHSH, VNX, khách; đo bằng: wrongful_carrier_faults, wrongful_refund_vnd, under_refund_vnd)
 └─ HOẶC
 ├─ [1] Độ trễ tính từ tracking thiếu ngày giao                              tầng: data
 │ └─ vì: delivered_date null nhưng status DELIVERED → db_delay_days tính tới hôm nay   bằng chứng: ticket S1-20@seed 11, S1-21@seed 11 (O-2120, O-2121)
 ├─ [2] Model dùng số ngày khách khai (ít hơn DB) rồi từ chối, không qua lệnh ghi   tầng: đầu vào / hành động
 │ └─ vì: model_override + agent trả lời từ chối trước mọi write_gate              bằng chứng: ticket S1-07@seed 11 (dòng 03, 05, 06)
 └─ [3] Không ai duyệt khi lỗi dồn về một hãng trong ngày                   tầng: vận hành / quyền hạn
 └─ vì: agent không đọc ops_limits (2 lỗi/hãng/ngày)                             bằng chứng: S1-42@11, S1-43@11 ở mốc base; carrier_fault_peak_per_day = 4 (R-S1-before-20261119-164457-9236c3)
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Không chạy lệnh ghi khi độ trễ không tính được từ tracking (kiện đã giao mà thiếu ngày giao) | Điểm phát nhập ngày giao ngay khi giao xong |
| [2] | Độ trễ chỉ lấy từ tracking DB; không được từ chối khi DB cho thấy khách được hoàn | Khách luôn khai trễ nhiều hơn thực tế, không bao giờ ít hơn |
| [3] | Từ lỗi thứ 3 của một hãng trong ngày phải có người duyệt (`ops_limits`) | Lỗi giao trễ rải đều, không dồn vào một hãng trong một ngày |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Kiện đã giao nhưng tracking thiếu `delivered_date` | `pre_guard`, nhánh P1: `status == "DELIVERED"` và không có `delivered_date` → `Verdict.escalate` (ghi sự kiện `tracking_incomplete`) | chặn | **Ngăn** khi `status` đã là DELIVERED: không lệnh ghi nào chạy. Chỉ **giảm** nếu cả `status` cũng chưa cập nhật | `R-S1-after-20261119-164601-7b75df` |
| [2] | Số ngày khách khai đè lên DB, rồi từ chối không qua lệnh ghi | `pre_guard`, nhánh P2: `Verdict.rewrite` bỏ "N ngày/hôm/tuần/days" khỏi chữ model đọc; `write_gate` khi `tool == "send_reply"` (G4): định trả lời 0đ mà `entitlement_vnd` theo DB > 0 → chuyển người | chặn | **Ngăn**: G4 so với quyền lợi tính từ tracking, không phụ thuộc cách khách viết. P2 một mình chỉ giảm (regex không bắt hết cách viết), nên G4 là lưới cuối | `R-S1-after-20261119-164601-7b75df` |
| [3] | Lỗi dồn về một hãng trong ngày, không ai duyệt | Giữ `write_gate` khi `tool == "file_carrier_fault"` (G2, vòng 1: trần `ops_limits.max_auto_strikes_per_carrier_per_day`); thêm metric `carrier_fault_peak_per_day` trong `monitors.py`; config không đổi | chặn + phát hiện | **Giảm**: trần đếm theo ngày, còn hợp đồng tính 3 lỗi/7 ngày, nên 2 lỗi/ngày trong 2 ngày vẫn có thể làm hãng bị tạm ngưng | `R-S1-after-20261119-164601-7b75df` |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `carrier_fault_peak_per_day` (chính) · `claim_vs_tracking_mismatch_rate` (phụ) |
| **Bước / hành vi được đo** | Lệnh ghi `file_carrier_fault` (chính); bước đọc độ trễ (phụ) |
| **Thước đo** (một câu, có đơn vị) | Số lỗi trợ lý tự ghi nhiều nhất cho **một** hãng trong **một** ngày vận hành (lỗi/hãng/ngày). Phụ: tỉ lệ ticket có số ngày khách khai lệch tracking hoặc tracking thiếu ngày giao (% ticket) |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `events` của trial: sự kiện `tool` với `tool = file_carrier_fault` và `carrier_id`; nhóm theo `seed` + `day`. Phụ: sự kiện `model_override` và sự kiện guard `claimed_days_removed`, `tracking_incomplete` |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Đếm số lỗi theo (seed, day, carrier_id), lấy giá trị lớn nhất; không có lỗi nào thì bằng 0. Phụ: số ticket có ít nhất một sự kiện trên ÷ tổng số ticket (mẫu số tối thiểu 1) |
| **Khung thời gian / ngưỡng báo động** | Cửa sổ 1 ngày vận hành. Vàng: 2 (chạm trần Ops). Đỏ: từ 3, hoặc hãng có `suspend_after_strikes_7d = 3` (GHSH, DNB) đã có 2 lỗi trong 7 ngày → NV-TUNG tắt `file_carrier_fault`, NV-OANH rà lại. Phụ: vàng > 0,30, đỏ > 0,50 |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không biết lỗi đúng hay oan; không cộng dồn 7 ngày như hợp đồng; lỗi do người ghi tay không được đếm. Phụ: không thấy khi chính tracking DB sai mà khách không khai số |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | `carrier_fault_peak_per_day`: bộ nền 1 · S1 base 4 → after 2. `claim_vs_tracking_mismatch_rate`: bộ nền 0,045 (base) / 0,23 (after) · S1 0,46 (base) / 0,62 (after) |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S1-after-20261119-164601-7b75df`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Hãng GHSH, VNX bị ghi lỗi sai và khách bị hoàn sai/thiếu
 └─ HOẶC
 ├─ [1] Tracking thiếu ngày giao VÀ [gate P1 (pre_guard) hỏng: status cũng chưa cập nhật]
 ├─ [2] Số khách khai lệch DB VÀ [gate P2 bỏ sót cách viết] VÀ [gate G4 (send_reply) hỏng]
 └─ [3] Lỗi dồn về một hãng VÀ [gate G2 trần ngày hỏng] (còn hở: cộng dồn 7 ngày của hợp đồng)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `pre_guard` P1; metric `claim_vs_tracking_mismatch_rate` | chặn + phát hiện | Ngăn khi `status` đúng, vì không lệnh ghi nào chạy trước khi người xem | `status` cũng sai; kiện `RETURNED`/`LOST` không có ngày giao |
| [2] | `pre_guard` P2 + `write_gate` `send_reply` G4 | chặn | Ngăn, vì G4 so với quyền lợi tính từ tracking DB, không đọc chữ khách | Chính tracking DB sai |
| [3] | `write_gate` `file_carrier_fault` G2 + metric `carrier_fault_peak_per_day` | chặn + phát hiện | Giảm, vì trần tính theo ngày | Cửa sổ 7 ngày của hợp đồng hãng |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Hãng nhỏ (GHSH, DNB: 3 lỗi/7 ngày là tạm ngưng) bị tạm ngưng tuyến vì lỗi tự ghi cộng dồn qua nhiều ngày, dù mỗi ngày đều dưới trần 2 | vừa | cao | Phùng Thị Nhài | `carrier_fault_peak_per_day` ≥ 2 trong ngày; tổng lỗi của hãng trong 7 ngày ≥ 2 (đếm từ bảng lỗi hãng, tới khi có metric 7 ngày) | Từ lỗi thứ 2 trong 7 ngày của hãng có ngưỡng 3: NV-HANH duyệt trước khi ghi; NV-OANH gửi bảng lỗi cho hãng mỗi ngày để hãng đối chiếu sớm | Nếu xảy ra trong pilot → Thu hẹp (tắt tự ghi lỗi cho hãng đó, chuyển người) | MANAGE |
| Tracking thiếu ngày giao tăng mạnh giờ cao điểm, làm tỉ lệ chuyển người vượt sức 1 người duyệt | vừa | vừa | Trần Thị Hà Anh | `claim_vs_tracking_mismatch_rate` > 0,50; tỉ lệ chuyển người > 0,33 (ngưỡng đã ký) | Báo hãng nhập ngày giao trong ca; gọi thêm người theo Runbook B7.6 | Nếu kéo dài → Thu hẹp về kho có tracking đầy đủ | MEASURE |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 Chất lượng | Xong | S1 after: pass_rate 1,0, 0 hoàn sai, 0 hoàn thiếu, 0 lỗi oan (`R-S1-after-20261119-164601-7b75df`); bộ nền 110/110 (`R-base-after-20261119-164602-7b75df`) | Nguyễn Nghiêm Khánh Tiệp |
| 2 Dữ liệu | Xong | C3.5: `delivered_date` không phải nguồn sự thật đầy đủ; cổng P1 kiểm `status` | Trần Thị Hà Anh |
| 5 Hiệu năng, hạ tầng | Chưa | Tỉ lệ chuyển người trên S1 tăng 0,1538 → 0,3077 (kể cả kiểm mẫu), vẫn 0 ca ùn; chưa đo giờ cao điểm thật | Phùng Thị Nhài |
| 7 Vận hành | Xong | 2 metric mới trong `lab10/monitors.py`; Runbook 4–5 dưới đây | Phùng Thị Nhài |
| 8 Con người, pháp lý | Xong | Lỗi ghi oan cho hãng trên S1: 30 → 5 → 0 (base → prepared → after) | Phùng Thị Nhài |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Dòng "Lỗi ghi oan cho hãng" ở Runbook 2 đã có, nhưng chỉ đo được khi có nhãn (sau khi hãng khiếu nại). Chưa có tín hiệu không cần nhãn: số lỗi của một hãng trong ngày, và tỉ lệ khách khai lệch tracking |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Thêm `carrier_fault_peak_per_day`: vàng 2, đỏ 3 (trước: không có). Thêm `claim_vs_tracking_mismatch_rate`: vàng > 0,30, đỏ > 0,50 (bộ nền 0,23). Không đổi ngưỡng trong `config/operating_gates.json` |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Không thêm người trực: 1 người vẫn 0 ca ùn, ROI trên S1 là 0,95. NV-OANH được gọi khi `carrier_fault_peak_per_day` chạm 2 |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Không đổi config. Quy trình mới: ca chuyển với lý do "thiếu ngày giao trong tracking" thì NV-HANH hỏi điểm phát ngày giao thật ngay trong ca |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | NV-OANH gửi GHSH trước 17h ngày 16/11/2026: danh sách lỗi đã rà, gỡ các lỗi không có ngày giao hoặc sai số ngày, hoàn tiền phạt. NV-TUNG gọi điều phối GHSH xác nhận không tạm ngưng tuyến. Với VNX: ghi bù lỗi thật của S1-07 sau khi đối chiếu |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Không có: `pii_leaks` = 0 ở cả ba mốc |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Qua phản hồi của người (email của hãng), không qua máy đo. Nguồn còn thiếu là chỉ số không cần nhãn; nay đã có `carrier_fault_peak_per_day` và `claim_vs_tracking_mismatch_rate` |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp 3 lần trong một giờ thì: NV-HANH xem hàng chờ; từ 4 ca hoặc chờ từ 30 phút thì gọi thêm 1 nhân viên CSKH; chờ quá 60 phút hoặc có 1 ca ùn thì NV-TUNG thu hẹp `pilot_scope` về kho HN.
2. Nếu nhà cung cấp LLM lỗi quá 15 phút thì: NV-TUNG tắt `issue_refund` trong `config/switches.json` (mọi ticket chuyển người; G1 vẫn chặn nhánh `fail_open`), báo nhóm Zalo; bật lại khi 15 phút liền không còn `llm_error`.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: NV-HANH ghi mã ticket vào nhóm Zalo; NV-OANH đối chiếu `decision_note` với tracking trong ngày; nếu quyết định sai thì xử lý như "hoàn sai > 0đ" ở Runbook 3, và tăng `review_sampling_pct` từ 10 lên 20 cho tới khi rà xong.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | phải giống v1: `53f8c62` (hash tiêu chí `106ca00f`) |
| Hash chốt cổng vòng 1 | phải giống v1: `74897172` |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: `R-S1-before-20261119-164945-7b75df` · prepared: `R-S1-prepared-20261119-164945-7b75df` · after: `R-S1-after-20261119-164945-7b75df` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không. Report: "Không vượt trần kinh doanh / vận hành nào." Trên S1 after: chờ lâu nhất 0 phút, 0 ca ùn, chi phí 5.116đ/ticket (làm tay 10.000đ), ROI 0,95, 0 lộ PII, 0 lỗi oan |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Kho **CT**: chi phí 7.053đ/ticket (cao nhất, do 2 ca chuyển người vì tracking thiếu ngày giao), vẫn rẻ hơn làm tay; pass_rate 1,0. Quyết định không đổi, và CT nằm ngoài 2 depot pilot |
| Quyết định (khoanh một) | **Tiếp tục** |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S1-after-20261119-164945-7b75df`: cả 5 ngưỡng bắt buộc đạt trên gói S1 (pass_rate 1,0; pass_k 1,0; hoàn sai 0đ; lỗi oan 0; PII 0) |
| Bằng chứng 2 | `R-base-after-20261119-164602-7b75df`: bộ nền 110/110, không regression. Ba ngưỡng `business_ops` đạt trên cả hai bộ (S1: 5.116đ, ROI 0,95, 0 ca ùn; bộ nền: 4.456đ, ROI 1,24, 0 ca ùn) |
| Bằng chứng 3 | Report tự kiểm tra `R-S1-grade-20261119-164944-7b75df`: "Mọi ngưỡng đã ký đều đạt · Được phép cân nhắc 'Tiếp tục'"; 5/5 mục chạy được trên máy đều xanh (integrity, criteria, visible, regression, monitor) |
| Khớp dòng nào trong `decision_rule` đã ký? | "Tiếp tục": cả 5 ngưỡng bắt buộc đạt trên bộ nền VÀ trên gói sự cố, cả 3 ngưỡng `business_ops` đạt, và report không còn dòng vượt trần nào |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | Không áp dụng. Pilot giữ đúng phạm vi đề xuất của Gate 1: 2 depot HN + HCM, 100% ticket giao trễ đơn lẻ, 1 người trực (NV-HANH) |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | Không áp dụng |
| Nếu Dừng: bài học ghi lại | Không áp dụng |
| Ngày quyết định lại (trừ khi Dừng) | 28/11/2026 (trước khi REFUND-v4 có hiệu lực), hoặc sớm hơn ngay khi `carrier_fault_peak_per_day` chạm 3 hay có 1 chỉ số an toàn lớn hơn 0 trong pilot |
| PIC ký | Trần Thị Hà Anh |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: **Đổi** từ Thu hẹp sang Tiếp tục. Ở v1, vế còn thiếu của dòng "Tiếp tục" là "đạt trên gói sự cố". Nay đã đo được: trên S1 after, pass_rate 1,0, hoàn sai 0đ, lỗi oan 0 (prepared là 0,7692 · 275.000đ · 5). Phạm vi pilot với khách thật vẫn là 2 depot như đề xuất.
- Report tự kiểm tra: mã lần chạy `R-S1-grade-20261119-164944-7b75df` · ô nào còn đỏ (nguyên nhân × tầng): không ô nào đỏ; ô `4 hidden` chưa chạy trên máy bàn (team chấm chạy sau buổi học).
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: Đỡ được 10/13 ticket và 25/30 lỗi oan (G1 với khách khai nhiều hơn DB, G2 với lỗi dồn trong ngày). Bỏ sót: khách khai ít hơn DB (không có lệnh ghi để cổng chạy) và tracking thiếu ngày giao.
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: "Được phép cân nhắc Tiếp tục"; quyết định Tiếp tục khớp.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: Lỗi của một hãng cộng dồn qua 7 ngày (hợp đồng tạm ngưng khi đủ 3 lỗi), và bài kiểm tra ẩn với đơn mới, cách viết khác. Nếu pilot lộ một chỉ số an toàn lớn hơn 0 thì quay về Thu hẹp theo `stop_condition` đã ký.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Điểm phát luôn nhập `delivered_date` ngay khi giao và `status` luôn khớp với nó; nếu cả hai cùng chưa cập nhật (nhập bù cuối ngày, giờ cao điểm) thì độ trễ vẫn bị tính tới hôm nay và hãng vẫn có thể bị ghi lỗi oan.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: NGĂN với nhánh khách khai lệch DB (G4 so với quyền lợi tính từ tracking, không đọc chữ khách) và nhánh kiện đã giao thiếu ngày giao (P1 chặn trước mọi lệnh ghi); chỉ GIẢM với nhánh lỗi dồn về một hãng, vì trần G2 tính theo ngày còn hợp đồng tính 3 lỗi/7 ngày, và vì mọi cổng đều tin chính tracking DB.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Tỉ lệ kiện đã giao mà thiếu `delivered_date` theo từng hãng và từng giờ (mock S1 có 2/13 đơn); số lỗi tự ghi cho mỗi hãng trong 7 ngày so với ngưỡng tạm ngưng; và tỉ lệ ca chuyển người thực tế (S1 tăng 0,15 → 0,31) so với sức duyệt 6 ca/giờ của NV-HANH.
