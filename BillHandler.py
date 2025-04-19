import os


class BillHandler:
    __billingList = "data/billingList.txt"

    if not os.path.exists(__billingList):
        with open(__billingList, "w") as file:
            pass

    @staticmethod
    def add_bill(subtotalBill: int) -> None:
        with open(BillHandler.__billingList, "a") as file:
            file.write(f"{subtotalBill}\n")

    @staticmethod
    def delete_bill(reservationNumber: int) -> None:
        with open(BillHandler.__billingList, "r") as file:
            billLines = file.readlines()

        with open(BillHandler.__billingList, "w") as file:
            for currentLine, line in enumerate(billLines, start=1):
                if currentLine != reservationNumber:
                    file.write(line)

    @staticmethod
    def calculate_subtotal_bill(numOfAdults: int, numOfChildren: int) -> int:
        PRICE_PER_ADULT = 500
        PRICE_PER_CHILD = 300
        return (numOfAdults * PRICE_PER_ADULT) + (numOfChildren * PRICE_PER_CHILD)

    @staticmethod
    def get_subtotal_bill(currentLineNumber: int) -> str | None:
        with open(BillHandler.__billingList, "r") as file:
            for currentLine, line in enumerate(file, start=1):
                if currentLine == currentLineNumber:
                    return line
        return None

    @staticmethod
    def get_grandtotal_bill() -> int:
        grandtotal = 0
        with open(BillHandler.__billingList, "r") as file:
            for currentLine, line in enumerate(file, start=1):
                grandtotal += int(line)

        return grandtotal
