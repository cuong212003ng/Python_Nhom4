# Chương trình Quản lý Khách hàng (Python)

## Mô tả
Chương trình cho phép quản lý thông tin khách hàng với các chức năng:
- Nhập thông tin khách hàng
- Xóa thông tin khách hàng
- Cập nhật thông tin khách hàng
- Tìm kiếm thông tin khách hàng
- Hiển thị danh sách khách hàng

## Cách chạy chương trình
1. Cài đặt Python 3 nếu chưa có.
2. Mở terminal/cmd, chuyển vào thư mục `Nhom4_242451101`.
3. Chạy lệnh:

```bash
python main.py
```

## Cấu trúc thư mục
- `main.py`: Chương trình chính, chứa giao diện menu tương tác với người dùng. File này xử lý việc nhập liệu từ người dùng và điều hướng đến các chức năng tương ứng trong CustomerManager.
- `customer.py`: Định nghĩa lớp Customer với các thuộc tính cơ bản của khách hàng như ID, tên, địa chỉ, số điện thoại và email. Lớp này cũng cung cấp phương thức __str__ để hiển thị thông tin khách hàng.
- `customer_manager.py`: Lớp quản lý danh sách khách hàng, cung cấp các phương thức để thêm, xóa, cập nhật, tìm kiếm và lấy danh sách khách hàng. Dữ liệu được lưu trữ trong bộ nhớ dưới dạng list. 