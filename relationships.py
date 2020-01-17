class Bank:
    def __init__(self, name):
        self.business_name = name
        self.customers = list()

first_tennessee = Bank("First Tennessee")

class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

mo = Customer("Mo", "Silvera")
warner = Customer("Warner", "Carpenter")
ken = Customer("Ken", "Perkerwicz")

first_tennessee.customers.append(mo)
first_tennessee.customers.append(warner)
first_tennessee.customers.append(ken)

for customer in first_tennessee.customers:
    print(f"{customer.first_name} {customer.last_name} is a customer of {first_tennessee.business_name}")