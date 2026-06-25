from vehicle_service import register_vehicle, list_available_vehicles, search_by_category
from customer_service import register_customer
from rental_service import create_rental, revenue_report


def menu():
    while True:
        print("\n" + "=" * 50)
        print("           DriveX — Vehicle Rental System")
        print("=" * 50)
        print("1. Register Vehicle")
        print("2. Register Customer")
        print("3. List Available Vehicles")
        print("4. Search Vehicles by Category")
        print("5. Create Rental")
        print("6. Revenue Report")
        print("0. Exit")
        print("-" * 50)

        option = input("Choose an option: ").strip()

        if option == "1":
            register_vehicle()
        elif option == "2":
            register_customer()
        elif option == "3":
            list_available_vehicles()
        elif option == "4":
            search_by_category()
        elif option == "5":
            create_rental()
        elif option == "6":
            revenue_report()
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print(" Invalid option. Please try again.")


if __name__ == "__main__":
    menu()
