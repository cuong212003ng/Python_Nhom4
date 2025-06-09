from customer import Customer
from customer_manager import CustomerManager

def print_menu():
    print("\n--- CHUONG TRINH QUAN LY KHACH HANG ---")
    print("1. Nhap thong tin khach hang")
    print("2. Xoa thong tin khach hang")
    print("3. Cap nhat thong tin khach hang")
    print("4. Tim kiem thong tin khach hang")
    print("5. Hien thi danh sach khach hang")
    print("0. Thoat")

def main():
    manager = CustomerManager()
    while True:
        print_menu()
        choice = input("Chon chuc nang: ")
        if choice == '1':
            customer_id = input("Nhap ma khach hang: ")
            name = input("Nhap ten khach hang: ")
            address = input("Nhap dia chi: ")
            phone = input("Nhap so dien thoai: ")
            email = input("Nhap email: ")
            customer = Customer(customer_id, name, address, phone, email)
            manager.add_customer(customer)
            print("Da them khach hang!")
        elif choice == '2':
            customer_id = input("Nhap ma khach hang can xoa: ")
            manager.remove_customer(customer_id)
            print("Da xoa khach hang!")
        elif choice == '3':
            customer_id = input("Nhap ma khach hang can cap nhat: ")
            name = input("Nhap ten moi (bo qua neu khong doi): ")
            address = input("Nhap dia chi moi (bo qua neu khong doi): ")
            phone = input("Nhap so dien thoai moi (bo qua neu khong doi): ")
            email = input("Nhap email moi (bo qua neu khong doi): ")
            updated = manager.update_customer(customer_id, name or None, address or None, phone or None, email or None)
            if updated:
                print("Da cap nhat khach hang!")
            else:
                print("Khong tim thay khach hang!")
        elif choice == '4':
            keyword = input("Nhap tu khoa tim kiem: ")
            results = manager.find_customer(keyword)
            if results:
                for c in results:
                    print(c)
            else:
                print("Khong tim thay khach hang!")
        elif choice == '5':
            for c in manager.get_all_customers():
                print(c)
        elif choice == '0':
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le!")

if __name__ == "__main__":
    main() 