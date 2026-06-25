from vehicle import Vehicle, Car, Motorcycle
from store import vehicles


def find_vehicle_by_plate(plate: str):
    for v in vehicles:
        if v.plate.upper() == plate.upper():
            return v
    return None


def register_vehicle():
    print("\n--- Register Vehicle ---")
    vehicle_type = input("Type (1 - Car / 2 - Motorcycle): ").strip()

    plate = input("Plate: ").strip().upper()
    if find_vehicle_by_plate(plate):
        print(f" A vehicle with plate {plate} already exists. Registration cancelled.")
        return

    brand = input("Brand: ").strip()
    model = input("Model: ").strip()
    daily_rate = float(input("Daily rate ($): "))

    if vehicle_type == "1":
        category = input("Category (SUV, Sedan, Hatch...): ").strip()
        vehicle = Car(plate, brand, model, daily_rate, category)
    elif vehicle_type == "2":
        engine_cc = int(input("Engine displacement in cc (e.g. 150): "))
        vehicle = Motorcycle(plate, brand, model, daily_rate, engine_cc)
    else:
        print(" Invalid type.")
        return

    vehicles.append(vehicle)
    print(f" Vehicle {brand} {model} registered successfully!")


def list_available_vehicles():
    print("\n--- Available Vehicles ---")
    available = [v for v in vehicles if v.available]

    if not available:
        print("No vehicles available at the moment.")
        return

    for v in available:
        print(v)


def search_by_category():
    print("\n--- Search by Category ---")
    category = input("Enter category (e.g. SUV, Sedan, Hatch): ").strip().lower()

    found = [v for v in vehicles if isinstance(v, Car) and v.category.lower() == category]

    if not found:
        print(f"No cars found in category '{category}'.")
        return

    for v in found:
        print(v)
