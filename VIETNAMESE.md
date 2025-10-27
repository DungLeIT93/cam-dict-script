# Hướng dẫn sử dụng - Oxford Dictionary Script cho Anki

## Giới thiệu
Script này giúp bạn tìm kiếm từ vựng trên Oxford Learner's Dictionary và xuất kết quả sang định dạng CSV để nhập vào Anki.

## Cài đặt

1. Clone repository này:
```bash
git clone https://github.com/DungLeIT93/oxford-dict-script.git
cd oxford-dict-script
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Cách sử dụng

### Tìm kiếm một từ

```bash
python oxford_dict.py hello
```

Kết quả sẽ hiển thị:
- Phiên âm
- Từ loại
- Định nghĩa
- Ví dụ

### Tìm kiếm nhiều từ cùng lúc

```bash
python oxford_dict.py hello world example beautiful
```

### Xử lý hàng loạt từ file

Tạo một file văn bản với mỗi từ trên một dòng (ví dụ: `danh-sach-tu.txt`):
```
hello
world
example
```

Sau đó tìm kiếm tất cả các từ từ file:
```bash
python oxford_dict.py -f danh-sach-tu.txt -o ket-qua.csv
```

Bạn cũng có thể kết hợp file với từ nhập trực tiếp:
```bash
python oxford_dict.py -f danh-sach-tu.txt hello world -o ket-qua.csv
```

### Xuất sang file CSV cho Anki

```bash
python oxford_dict.py -o tu-vung.csv hello world example
```

File CSV sẽ được tạo với tên `tu-vung.csv`

### Chế độ im lặng (không hiển thị trên màn hình)

```bash
python oxford_dict.py -q -o tu-vung.csv hello world
```

## Nhập vào Anki

1. Chạy lệnh để tạo file CSV:
   ```bash
   python oxford_dict.py -o tu-vung.csv beautiful amazing wonderful
   ```

2. Mở Anki và chọn: **File → Import** (hoặc **Tệp → Nhập**)

3. Chọn file CSV bạn vừa tạo (ví dụ: `tu-vung.csv`)

4. Cấu hình nhập:
   - **Type** (Loại): Basic (hoặc tạo note type riêng)
   - **Deck** (Bộ thẻ): Chọn bộ thẻ bạn muốn
   - **Fields separated by** (Phân tách bằng): Tab
   - **Allow HTML in fields** (Cho phép HTML): Bật (Có)

5. Ánh xạ các trường:
   - Trường 1: Từ vựng
   - Trường 2: Phiên âm
   - Trường 3: Từ loại
   - Trường 4: Định nghĩa
   - Trường 5: Ví dụ

6. Nhấn **Import** (Nhập)

## Xem ví dụ

Chạy file example.py để xem kết quả mẫu:

```bash
python example.py
```

File này sẽ tạo một file CSV mẫu (`sample_output.csv`) với dữ liệu demo để bạn hiểu cách script hoạt động.

## Cấu trúc dữ liệu xuất

Mỗi từ sẽ có 5 trường thông tin:
1. **Word** (Từ): Từ vựng cần tra
2. **Pronunciation** (Phiên âm): Phiên âm IPA
3. **Part of Speech** (Từ loại): danh từ, động từ, tính từ, v.v.
4. **Definitions** (Định nghĩa): Danh sách các định nghĩa (đánh số)
5. **Examples** (Ví dụ): Các câu ví dụ

## Lưu ý

- Cần kết nối Internet để tra từ
- Script tra từ từ Oxford Learner's Dictionary
- Mỗi từ sẽ lấy tối đa 5 định nghĩa và 3 ví dụ
- Định dạng xuất là Tab-separated values (TSV) với HTML formatting

## Khắc phục sự cố

### Lỗi kết nối
Kiểm tra kết nối Internet và đảm bảo có thể truy cập được trang https://www.oxfordlearnersdictionaries.com/

### Không tìm thấy từ
- Kiểm tra chính tả
- Thử tra từ gốc (ví dụ: "run" thay vì "running")
- Một số từ chuyên ngành hoặc hiếm có thể không có trong từ điển học tập

### Lỗi khi nhập vào Anki
- Đảm bảo bật "Allow HTML in fields"
- Kiểm tra field separator là "Tab"
- Xác nhận file CSV đã được tạo thành công

## Ví dụ sử dụng thực tế

### Ví dụ 1: Học từ vựng chủ đề cảm xúc
```bash
python oxford_dict.py -o cam-xuc.csv happy sad angry excited worried
```

### Ví dụ 2: Học động từ thường dùng
```bash
python oxford_dict.py -o dong-tu.csv run walk eat drink sleep work study
```

### Ví dụ 3: Học tính từ miêu tả
```bash
python oxford_dict.py -o tinh-tu.csv beautiful ugly big small hot cold
```

## Hỗ trợ

Nếu có vấn đề hoặc câu hỏi, vui lòng tạo issue trên GitHub.
