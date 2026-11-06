#main menu and mode selection.
#Distance, speed, and time:
from calculations import calculate_distance, calculate_speed, calculate_time

def quick_mode():
    while True:
        print("\n===== AstroCalc: Quick Mode =====")
        print("1. Calculate Distance")
        print("2. Calculate Speed")
        print("3. Calculate Time")
        print("4. Return to Main Menu")

        choice = input("\nWhat would you like to calculate? ")

        if choice == "1":
            try:
                speed = float(input("Enter speed (km/s): "))
                time = float(input("Enter time (seconds): "))

                distance = calculate_distance(speed, time)
                print(f"\nDistance: {distance:,.2f} km")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "2":
            try:
                distance = float(input("Enter distance (km): "))
                time = float(input("Enter time (seconds): "))

                if time == 0:
                    print("Time cannot be zero.")
                else:
                    speed = calculate_speed(distance, time)
                    print(f"\nSpeed: {speed:,.2f} km/s")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            try:
                distance = float(input("Enter distance (km): "))
                speed = float(input("Enter speed (km/s): "))

                if speed == 0:
                    print("Speed cannot be zero.")
                else:
                    time = calculate_time(distance, speed)
                    print(f"\nTime: {time:,.2f} seconds")
                    print(f"Time: {time / 60:,.2f} minutes")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")


quick_mode()