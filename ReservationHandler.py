import os
from BillHandler import BillHandler
from CustHandler import CustHandler


class Reservation:
    def __init__(
        self, date: str, time: str, name: str, numOfAdults: int, numOfChildren: int
    ):
        self.__date = date
        self.__time = time
        self.__name = name
        self.__numOfAdults = numOfAdults
        self.__numOfChildren = numOfChildren

    def get_date(self) -> str:
        return self.__date

    def get_time(self) -> str:
        return self.__time

    def get_name(self) -> str:
        return self.__name

    def get_numOfAdults(self) -> int:
        return self.__numOfAdults

    def get_numOfChildren(self) -> int:
        return self.__numOfChildren


class ReservationList:
    __reservationList = "data/reservationList.txt"

    if not os.path.exists(__reservationList):
        with open(__reservationList, "w") as file:
            pass

    def view_reservations(self) -> None:
        if os.path.getsize(self.__reservationList) == 0:
            print("No Reservations.\n")
            return

        with open(self.__reservationList, "r") as file:
            for currentLine, line in enumerate(file, start=1):
                if currentLine == 1:
                    print("#\tDate\tTime\tName\tAdults\tChildren".expandtabs(18))
                if line:
                    print(f"{currentLine}\t{line.rstrip()}")

    def add_reservation(self, res: Reservation) -> None:
        date = res.get_date()
        time = res.get_time()
        name = res.get_name()
        numOfAdults = res.get_numOfAdults()
        numOfChildren = res.get_numOfChildren()
        subtotalBill = BillHandler.calculate_subtotal_bill(numOfAdults, numOfChildren)

        with open(self.__reservationList, "a") as file:
            file.write(
                f"{date:<26} {time:<8} {name:<29} {numOfAdults:<18}{numOfChildren}\n"
            )

        CustHandler.add_cust(numOfAdults, numOfChildren)
        BillHandler.add_bill(subtotalBill)

    def delete_reservation(self, reservationNumber: int) -> None:
        with open(self.__reservationList, "r") as file:
            lines = file.readlines()
            if reservationNumber > len(lines) or reservationNumber <= 0:
                print("Reservation does not exist.")
                return

        with open(self.__reservationList, "w") as file:
            for currentLine, line in enumerate(lines, start=1):
                if currentLine != reservationNumber:
                    file.write(line)
                else:
                    print("Deleted reservation:")
                    print("#\tDate\tTime\tName\tAdults\tChildren".expandtabs(18))
                    print(f"{reservationNumber}\t{line.rstrip()}")

        CustHandler.delete_cust(reservationNumber)
        BillHandler.delete_bill(reservationNumber)

    def generate_report(self) -> None:
        if os.path.getsize(self.__reservationList) == 0:
            print("No Reservations.")

        with open(self.__reservationList, "r") as file:
            for currentLine, line in enumerate(file, start=1):
                if currentLine == 1:
                    print(
                        "#\tDate\tTime\tName\tAdults\tChildren\tSubtotal".expandtabs(18)
                    )

                print(
                    f"{currentLine}\t{line.rstrip()}\t{float(BillHandler.get_subtotal_bill(currentLine)):>20.2f}"
                )

        print(f"\nTotal number of Adults: {CustHandler.get_total_adult()}")
        print(f"Total number of Kids: {CustHandler.get_total_children()}")
        print(f"Grand Total: PHP{float(BillHandler.get_grandtotal_bill()):.2f}")
        print(
            "\n.....................................................nothing follows....................................................."
        )
