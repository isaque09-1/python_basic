class Customer:
    def __init__(self, cpf: str, name: str, license_number: str):
        self.cpf = cpf
        self.name = name
        self.license_number = license_number

    def __repr__(self):
        return f"CPF: {self.cpf} | Name: {self.name} | License: {self.license_number}"
