from pathlib import Path
import csv
import unicodedata


class InvalidCredentialException(Exception):
    pass
class UnknownUserException(Exception):
    pass
class InvalidPasswordException(Exception):
    pass

class ShortPasswordRegisterException(Exception):
    pass
class LoginExistsExeption(Exception):
    pass
class DifferentLoginLayoutExeption(Exception):
    pass
class DifferentPasswordLayoutExeption(Exception):
    pass
class TooLongPasswordRegisterException(Exception):
    pass

class Database:

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.data = []

    def __enter__(self):
        self.open_data()
        return self

    def __add__(self, username, password):
        self.add_data(username, password)
        return self

    def open_data(self):
        with open(self.file_path, mode='r', encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            self.data = [row for row in reader]

    def add_data(self, username, password):
        with open(self.file_path, mode='a',newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=['Login', 'Password'])
            writer.writerow({"Login": username, "Password": password})


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_data()

    def close_data(self):
        pass

    def __iter__(self):
        return iter(self.data)

    def has_different_layouts(self, text: str) -> bool:
        is_lat = any(unicodedata.name(char).startswith('LATIN') for char in text if char.isalpha())
        is_cyr = any(unicodedata.name(char).startswith('CYRILLIC') for char in text if char.isalpha())
        return is_lat and is_cyr



    def login(self, username: str, password: str) -> bool:

        if username is None or password is None:
            raise InvalidCredentialException

        user_found = False
        for line in self.data:
            if username == line["Login"]:

                user_found = True
                if password == line["Password"]:
                    return True
                else:
                    raise InvalidPasswordException

        if not user_found:
            raise UnknownUserException


    def register(self, username: str, password: str) -> bool:

        if username is None or password is None:
            raise InvalidCredentialException

        if len(password) < 2:
            raise ShortPasswordRegisterException
        if len(password) > 16:
            raise TooLongPasswordRegisterException

        if self.has_different_layouts(username):
            raise DifferentLoginLayoutExeption

        if self.has_different_layouts(password):
            raise DifferentPasswordLayoutExeption

        for line in self.data:
            if username == line["Login"]:
                raise LoginExistsExeption
        else:
            self.add_data(username, password)
            return True



users = Database(Path("data.csv"))
"""
with users as db:
    for row in db:
        print(row)
print(users.login("UserTest", "PassTest"))
users.register("George", "GeorgePassword")
"""
