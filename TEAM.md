# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): DongSongLoiThe
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-DongSongLoiThe-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S1

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Trần Thị Hà Anh | 2A202603887 | Sản phẩm và kinh doanh | v |
|   2 | Nguyễn Nghiêm Khánh Tiệp | 2A202603863 | Kỹ sư cổng |             |
|   3 | Phùng Thị Nhài | 2A202603725 | Vận hành và pháp lý |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TranThiHaAnh-2A202603887

### Phần việc phụ trách

Trưởng nhóm · vai **Sản phẩm và kinh doanh**.
- Đề bài: câu 1.1, 1.5 (cùng cả bàn), 1.6 và ký tiêu chí; câu 2.3, 2.9; quyết định v1; câu 3.2; quyết định v2.
- Phiếu: A mục A1 (câu 1.1), A3, A4, A5; B mục B3, B7.4, B8; C mục C5 (câu 3.2), C12.
- File: `config/acceptance_criteria.json` (+ `.lock`), `config/operating_gates.json` mục `business`, `submission/submission.json` (quyết định v1, v2), `TEAM.md` (thông tin nhóm, bảng thành viên).

### Đóng góp cụ thể

- Viết Bản tiêu chí: 5 ngưỡng bắt buộc (pass_rate ≥ 0,94, pass_k ≥ 0,86, ba chỉ số an toàn = 0), `escalation_rate` ≤ 0,33, nhóm `business_ops` (≤ 7.500đ/ticket, ROI ≥ 0,3, 0 ca ùn) suy từ `ops_facts`, `stop_condition` và `decision_rule` cho cả bốn quyết định; nới ngưỡng một lần **trước khi ký**, rồi ký trước lần đánh giá đầu tiên.
- Bản đồ dữ liệu và ví dụ drift REFUND-v4 (01/12/2026): cờ `index_active` là bản sao do người bật tay; dẫn tới cổng P0 ghim chính sách theo ngày hiệu lực.
- Đặt cổng kinh doanh: trần hoàn tự động 1.000.000đ/ngày (½ ngân sách Finance), ngân sách 1.500đ/ticket (trần LLM), phạm vi `all` sau khi so lần chạy thử 2 depot (ROI 1,24 so với 0,80).
- Quyết định v1 **Thu hẹp** (chưa có bằng chứng trên gói sự cố) và v2 **Tiếp tục** (S1 after đạt mọi ngưỡng đã ký, report "được phép cân nhắc Tiếp tục").
- Viết specification của thẻ S1 (câu 3.2) và ba dòng bắt buộc.

### Bằng chứng

- Commit: `1aa78eb` (bước 0), `95ed23c` (bản nháp tiêu chí, Phiếu A mục A4), `53f8c62` (Sign acceptance criteria, hash `106ca00f`), `bf57a74` (Phiếu A mục A5), `3c9bbea` (chốt vòng 1, quyết định v1), `5858665` (nhận thẻ S1), commit nộp bài cuối (Phiếu C, quyết định v2).
- Lần chạy: `R-base-before-20261119-152757-bde05c` (base, `lab10.gate` CHƯA đạt 2 ngưỡng an toàn), `R-base-after-20261119-153103-eb912c` (thử phạm vi 2 depot), `R-base-prepared-20261119-154212-d19f72` (bằng chứng v1), `R-S1-grade-20261119-164944-7b75df` (bằng chứng v2).
- Phiếu: A mục A1 câu 1.1, A4, A5; B mục B3, B7.4, B8; C mục C5 câu 3.2, C12.

### Exit ticket

- Học được: ngưỡng phải viết và ký trước khi nhìn số; chính dòng `decision_rule` đã ký buộc bàn chọn Thu hẹp ở v1 dù bộ nền đã xanh, vì vế "đạt trên gói sự cố" chưa đo được.
- Chưa chắc: ngưỡng ROI ≥ 0,3 và 7.500đ/ticket có còn hợp lý khi mở rộng 12 depot và REFUND-v4 hạ hạn mức tự động xuống 100.000đ hay không.

## NguyenNghiemKhanhTiep-2A202603863

### Phần việc phụ trách

Vai **Kỹ sư cổng**.
- Đề bài: câu 1.3; câu 2.1, 2.2, 2.6, 2.7, 2.8; câu 3.1 (dò trace), 3.5 (phần code), 3.6; chạy ba mốc base · prepared · after.
- Phiếu: A mục A2 (cột Offline, câu 1.3); B mục B0, B1, B2, B7.1, B7.2, B7.3; C mục C0, C2, C7 (phần code), C8; cùng cả bàn ở C6, C9.
- File: `lab10/guards.py`, `lab10/monitors.py`.

### Đóng góp cụ thể

- Thiết kế offline metric cho bước ghi lỗi hãng: tỉ lệ lần chạy ghi lỗi oan trên số lần chạy có `file_carrier_fault`.
- Chạy mốc base và dò `T-002@55`: xếp hai lỗi chìm (số ngày khách khai đè DB; `customer_note` gửi sang hãng).
- Code cổng vòng 1: P0 (`pre_guard` ghim chính sách theo ngày hiệu lực), G1 (`issue_refund`: số tiền, người trả, căn cứ, phê duyệt khớp DB; không hoàn hai lần), G2 (`file_carrier_fault`: đúng kiện, đúng hãng, đúng số ngày, trần 2 lỗi/hãng/ngày), G3 (`notify_carrier`: chỉ gửi trường chính sách cho phép). Bộ nền 0,9909 → 1,0, không ca nào hỏng.
- Behavioral test với 2 ticket hiểm (khách khai 12 ngày ở O-1001; đơn quà tặng O-1026) và 1 ticket dự phòng cài lệnh (O-1021).
- Vòng 2 (thẻ S1): dò `S1-07@11`, `S1-20@11`; thêm P1 (kiện đã giao thiếu `delivered_date` → chuyển người), P2 (bỏ số ngày khách tự khai), G4 (`send_reply`: không từ chối khi DB cho hoàn); thêm 2 chỉ số `carrier_fault_peak_per_day`, `claim_vs_tracking_mismatch_rate`. Gói S1 0,7692 → 1,0; lỗi oan 5 → 0.

### Bằng chứng

- Commit: `5e5f463` (Phiếu A câu 1.3; commit bằng tên git chung của bàn là mã trưởng nhóm), `3c9bbea` (cổng vòng 1, bản chốt `74897172`), commit nộp bài cuối (`lab10/guards.py`, `lab10/monitors.py` vòng 2).
- Lần chạy: `R-base-before-20261119-152757-bde05c`, `R-base-after-20261119-152930-af9ae7` (4 cổng code), `R-S1-prepared-20261119-164457-9236c3`, `R-S1-after-20261119-164601-7b75df`, `R-base-after-20261119-164602-7b75df` (không regression), grade `R-S1-grade-20261119-164944-7b75df` (6 monitor ✅).
- Phiếu: A mục A2 cột Offline; B mục B0–B2, B7.1–B7.3; C mục C0, C2, C7, C8.

### Exit ticket

- Học được: cổng chỉ chặn ở lệnh ghi thì bỏ sót lỗi "không làm gì" (S1-07 từ chối mà không gọi lệnh ghi nào), nên cần cả cổng trước khi model đọc và cổng ở câu trả lời cho khách.
- Chưa chắc: regex bỏ số ngày khách khai (P2) có bắt được mọi cách viết trong bài kiểm tra ẩn không; hiện G4 là lưới cuối nhưng chỉ chuyển người chứ không tự hoàn đúng.

## PhungThiNhai-2A202603725

### Phần việc phụ trách

Vai **Vận hành và pháp lý**.
- Đề bài: câu 1.2, 1.4; câu 2.4, 2.10; câu 3.1 (phần riêng của thẻ), 3.3, 3.7; cùng cả bàn ở pre-mortem (2.5) và mốc prepared (3.0).
- Phiếu: A mục A1 (câu 1.2), A2 (cột Telemetry production, câu 1.4); B mục B4, B5, B6 (cùng cả bàn), B7.5, B7.6; C mục C1 (cùng cả bàn), C3.5, C4, C5 (câu 3.3), C9, C10, C11.
- File: `config/operating_gates.json` mục `operations` và `legal`; `submission/submission.json` (gom bài).

### Đóng góp cụ thể

- Mục tiêu nhìn từ chị Oanh (sổ khớp với hãng và shop, 0 dòng phải gỡ) và chị Hạnh (ca chuyển sang được nhận trong 60 phút, có lý do chuyển); telemetry production cho `file_carrier_fault` (số lỗi/hãng/24 giờ, lỗi không khớp tracking; vàng 2, đỏ 3).
- HAZOP vòng 1 trên `file_carrier_fault` (6 dòng, gồm nhánh chưa thấy trên trace: ghi lỗi cho `parcels[0]` thay vì kiện trễ) và 4 dòng ngoài kỹ thuật (người duyệt, ngân sách, phạm vi pilot, dữ liệu gửi bên thứ ba); checklist 9 nhóm việc có PIC từng dòng.
- Đặt cổng vận hành, pháp lý: PIC NV-TUNG, người duyệt NV-HANH, 1 người trực × 6 ca/giờ, chờ tối đa 60 phút, `decision_note = true`, kiểm mẫu 10% (đúng điều kiện tin của nhân viên), chặn 5 trường dữ liệu cá nhân gửi hãng, lỗi hãng phải có nguyên nhân trong tracking; runbook phần 1–3 và giờ cao điểm khớp các con số đó.
- Vòng 2 (thẻ S1): mở lại bản đồ dữ liệu (`delivered_date` không phải nguồn sự thật đầy đủ; `status` là tín hiệu kiểm), HAZOP của thẻ (4 dòng), giả định môi trường, fault tree sau khi sửa, 2 dòng risk register, cập nhật checklist, runbook phần 4–5; điền `submission.json`.

### Bằng chứng

- Commit: `9ac0053` (Phiếu A câu 1.2, 1.4), `3c9bbea` (config `operations`, `legal`; Phiếu B mục B4, B5, B7.5, B7.6), commit nộp bài cuối (Phiếu C mục C3.5, C4, C9–C11; `submission/submission.json`).
- Lần chạy: `R-base-after-20261119-153025-d19f72` (cổng config: chuyển người 0,2727, 0 ca ùn, ROI 1,24), `R-S1-after-20261119-164601-7b75df` (lỗi oan cho hãng 30 → 0), grade `R-S1-grade-20261119-164944-7b75df`.
- Phiếu: A mục A1 câu 1.2, A2 cột Telemetry; B mục B4, B5, B7.5, B7.6; C mục C3.5, C4, C5 câu 3.3, C9, C10, C11.

### Exit ticket

- Học được: tác hại lớn nhất rơi vào bên thứ ba không dùng trợ lý (hãng GHSH, 12 tài xế), và nó lộ ra qua email khiếu nại chứ không qua máy đo; cần chỉ số không cần nhãn như số lỗi/hãng/ngày.
- Chưa chắc: một người trực (NV-HANH, 6 ca/giờ) có đủ khi tỉ lệ chuyển người trên S1 đã tăng 0,15 → 0,31 và giờ cao điểm gấp ba hay không; mock chưa đo được.
