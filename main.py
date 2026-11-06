#main menu and mode selection.
#Distance, speed, and time:
from calculations import (
    calculate_distance,
    calculate_speed,
    calculate_time,
    calculate_scaled_distance
)


def quick_mode():
    while True:
        print("\n===== AstroCalc: Quick Mode =====")
        print("1. Calculate Distance")
        print("2. Calculate Speed")
        print("3. Calculate Time")
        print("4. Solar System Scale Calculator")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            speed = float(input("Enter speed (km/s): "))
            time = float(input("Enter time (seconds): "))
            print(f"Distance: {calculate_distance(speed, time):,.2f} km")

        elif choice == "2":
            distance = float(input("Enter distance (km): "))
            time = float(input("Enter time (seconds): "))

            if time == 0:
                print("Time cannot be zero.")
            else:
                print(f"Speed: {calculate_speed(distance, time):,.2f} km/s")

        elif choice == "3":
            distance = float(input("Enter distance (km): "))
            speed = float(input("Enter speed (km/s): "))

            if speed == 0:
                print("Speed cannot be zero.")
            else:
                print(f"Time: {calculate_time(distance, speed):,.2f} seconds")

        elif choice == "4":
            strip_length = float(input("Enter strip length (cm): "))

            print("\nSolar System Scaled Distances")

            objects = {
                "Mercury": 5.83e7,
                "Venus": 1.08e8,
                "Earth": 1.50e8,
                "Mars": 2.27e8,
                "Asteroid Belt (inner edge)": 3.28e8,
                "Asteroid Belt (outer edge)": 4.77e8,
                "Jupiter": 7.78e8,
                "Saturn": 1.43e9,
                "Uranus": 2.87e9,
                "Neptune": 4.50e9,
                "Pluto": 5.91e9
            }

            for name, distance in objects.items():
                scaled = calculate_scaled_distance(distance, strip_length)
                print(f"{name:30} {scaled:8.2f} cm")

        elif choice == "5":
            print("Thank you for using AstroCalc!")
            break

        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    quick_mode()