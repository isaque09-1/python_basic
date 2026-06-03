from customer import Customer
from store import customers


def find_customer_by_cpf(cpf: str):
    for c in customers:
        if c.cpf == cpf:
            return c
    return None


def register_customer():
    print("\n--- Register Customer ---")
    cpf = input("CPF: ").strip()

    if find_customer_by_cpf(cpf):
        print(f" A customer with CPF {cpf} already exists. Registration cancelled.")
        return

    name = input("Name: ").strip()
    license_number = input("Driver's License Number: ").strip()

    customer = Customer(cpf, name, license_number)
    customers.append(customer)
    print(f" Customer {name} registered successfully!")
