from ReservationHandler import ReservationList
from ReservationHandler import Reservation
from InputValidator import InputValidator

RUNNING = True
resList = ReservationList()
divider = "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
divider = divider * 4 + "="

print("Dionisio, Zion Nathan | 2BSIT-1")

print("RESTAURANT RESERVATION SYSTEM")
print(divider)

while RUNNING:
    print("System Menu")
    print("a. View All Reservations")
    print("b. Make Reservation")
    print("c. Delete Reservation")
    print("d. Generate Report")
    print("e. Exit")
    choice = input("Enter choice: ")
    print(divider)

    match choice.lower():
        case "a":
            resList.view_reservations()
        case "b":
            date = InputValidator.is_valid_date(
                input("Enter reservation date: ").strip()
            )

            if not date:
                print("Invalid date, please try again.")
                continue

            time = InputValidator.is_valid_time(
                input("Enter reservation time: ").strip()
            )

            if not time:
                print("Invalid time, please try again.")
                continue

            name = InputValidator.is_valid_name(
                input("Reservation shall be named under: ").strip()
            )

            if not name:
                print("Invalid name, please try again.")
                continue

            numOfAdult = InputValidator.is_valid_number(
                input("Enter number of expected adults: ").strip()
            )

            if not numOfAdult:
                print("Invalid number, please try again.")
                continue

            numOfChildren = InputValidator.is_valid_number(
                input("Enter number of expected children: ").strip()
            )

            if not numOfChildren:
                print("Invalid number, please try again.")
                continue

            newReservation = Reservation(
                date, time, name, int(numOfAdult), int(numOfChildren)
            )
            resList.add_reservation(newReservation)
        case "c":
            resNumToDelete = int(input("Enter reservation number to delete: ").strip())
            resList.delete_reservation(resNumToDelete)
        case "d":
            resList.generate_report()
        case "e":
            print("Thank You!")
            break
        case _:
            print("Not an option, please try again.\n")
    print(divider)
