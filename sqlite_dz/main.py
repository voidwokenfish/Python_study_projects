from pathlib import Path
import unicodedata
import sqlite3



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




class UsersRepository:
    def __init__(self, db_path: Path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        #self.table_name = self.cursor.execute()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        login TEXT NOT NULL,
        password TEXT NOT NULL
        )
        ''')
        self.connection.commit()



    def get_by_login(self, login: int):
        if login is None:
            raise InvalidCredentialException
        self.cursor.execute("SELECT login, password from Users WHERE login=?", (login,))
        result = self.cursor.fetchone()

        return result

    def add_user(self, username: str, password: str):
        if username is None or password is None:
            raise InvalidCredentialException
        self.cursor.execute("INSERT INTO Users (login, password) VALUES (?, ?)", (username, password))
        self.connection.commit()
        return True

    def has_different_layouts(self, text: str) -> bool:
        is_lat = any(unicodedata.name(char).startswith('LATIN') for char in text if char.isalpha())
        is_cyr = any(unicodedata.name(char).startswith('CYRILLIC') for char in text if char.isalpha())
        return is_lat and is_cyr

class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def do_login(self, repo: UsersRepository) -> bool:
        user = repo.get_by_login(self.login)
        if user is None:
            raise UnknownUserException
        if user[1] != self.password:
            raise InvalidPasswordException
        return True

    def register(self, repo: UsersRepository):
        user = repo.get_by_login(self.login)
        if user:
            raise LoginExistsExeption

        if len(self.password) < 2:
            raise ShortPasswordRegisterException
        if len(self.password) > 16:
            raise TooLongPasswordRegisterException

        if sql_db.has_different_layouts(self.login):
            raise DifferentLoginLayoutExeption
        if sql_db.has_different_layouts(self.password):
            raise DifferentPasswordLayoutExeption


        repo.add_user(self.login, self.password)
        return True



sql_db = UsersRepository(Path("my_database.db"))
user = User( "KittyCat", "NyanNyan")
#user.do_login(sql_db)
#user.register(sql_db)
sql_db.create_table()


