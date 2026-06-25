from rental import Rental
from store import rentals
from customer_service import find_customer_by_cpf
from vehicle_service import find_vehicle_by_plate


def create_rental():
    print("\n--- Create Rental ---")

    cpf = input("Customer CPF: ").strip()
    customer = find_customer_by_cpf(cpf)
    if not customer:
        print("Customer not found. Please register the customer first.")
        return

    plate = input("Vehicle plate: ").strip().upper()
    vehicle = find_vehicle_by_plate(plate)
    if not vehicle:
        print(" Vehicle not found.")
        return

    if not vehicle.available:
        print(f" Vehicle {vehicle.model} (plate {plate}) is not available.")
        return

    days = int(input("Number of days: "))

    vehicle.available = False
    rental = Rental(customer, vehicle, days)
    rentals.append(rental)

    print(f"\n Rental created successfully!")
    print(f"   Total to pay: ${rental.calculate_total():.2f}")


def revenue_report():
    print("\n--- Revenue Report ---")

    if not rentals:
        print("No rentals registered.")
        return

    total = 0.0
    for rental in rentals:
        print(rental)
        print("-" * 50)
        total += rental.calculate_total()

    print(f"\n Total gross revenue: ${total:.2f}")
