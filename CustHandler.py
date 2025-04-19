import os


class CustHandler:
    __custNumList = "data\\custNumList.txt"

    if not os.path.exists(__custNumList):
        with open(__custNumList, "w") as file:
            pass

    @staticmethod
    def add_cust(numOfAdults, numOfChildren) -> None:
        with open(CustHandler.__custNumList, "a") as file:
            file.write(f"{numOfAdults}\n")
            file.write(f"{numOfChildren}\n")

    @staticmethod
    def delete_cust(reservationNumber) -> None:
        with open(CustHandler.__custNumList, "r") as file:
            billLines = file.readlines()

        lineToDelete = reservationNumber * 2

        with open(CustHandler.__custNumList, "w") as file:
            for currentLine, line in enumerate(billLines, start=1):
                if currentLine != lineToDelete and currentLine != lineToDelete - 1:
                    file.write(line)

    @staticmethod
    def get_total_adult() -> int:
        totalAdults = 0
        with open(CustHandler.__custNumList, "r") as file:
            custLines = file.readlines()

            for currentLine, line in enumerate(custLines, start=1):
                if currentLine % 2 != 0:
                    totalAdults += int(line.rstrip())

        return totalAdults

    @staticmethod
    def get_total_children() -> int:
        totalChildren = 0
        with open(CustHandler.__custNumList, "r") as file:
            custLines = file.readlines()

            for currentLine, line in enumerate(custLines, start=1):
                if currentLine % 2 == 0:
                    totalChildren += int(line.rstrip())

        return totalChildren
