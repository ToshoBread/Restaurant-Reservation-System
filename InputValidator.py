from datetime import datetime


class InputValidator:
    @staticmethod
    def is_valid_date(date: str) -> str | None:
        try:
            date = date.title()
            verifiedDate = datetime.strptime(date, "%B %d, %Y")

            if verifiedDate > datetime.now():
                return date
            else:
                return None
        except ValueError:
            return None

    @staticmethod
    def is_valid_time(time: str) -> str | None:
        try:
            datetime.strptime(time.upper(), "%I:%M%p")
            return time.lower()
        except ValueError:
            return None

    @staticmethod
    def is_valid_name(name: str) -> str | None:
        if not any(char.isnumeric() for char in name):
            return name.title()
        return None

    @staticmethod
    def is_valid_number(number: str) -> int | None:
        if not number.isdigit():
            return None

        if 0 <= int(number) <= 99:
            return int(number)

        return None
