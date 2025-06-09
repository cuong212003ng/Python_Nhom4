class Customer:
    def __init__(self, customer_id, name, address, phone, email):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"ID: {self.customer_id}, Name: {self.name}, Address: {self.address}, Phone: {self.phone}, Email: {self.email}" 