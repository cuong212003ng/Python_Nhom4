from customer import Customer

class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer_id):
        self.customers = [c for c in self.customers if c.customer_id != customer_id]

    def update_customer(self, customer_id, name=None, address=None, phone=None, email=None):
        for c in self.customers:
            if c.customer_id == customer_id:
                if name: c.name = name
                if address: c.address = address
                if phone: c.phone = phone
                if email: c.email = email
                return True
        return False

    def find_customer(self, keyword):
        return [c for c in self.customers if keyword.lower() in c.name.lower() or keyword.lower() in c.customer_id.lower()]

    def get_all_customers(self):
        return self.customers 