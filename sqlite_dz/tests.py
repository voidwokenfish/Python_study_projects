from pathlib import Path
import sqlite3
import unittest



from main import UsersRepository, User, InvalidCredentialException, InvalidPasswordException, UnknownUserException, LoginExistsExeption, DifferentLoginLayoutExeption, DifferentPasswordLayoutExeption, ShortPasswordRegisterException, TooLongPasswordRegisterException

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.test_db = UsersRepository(Path(Path("testbase.db")))
        self.test_db.create_table()
        self.test_db.connection.commit()
        self.test_user = User("ManChainArgo", "BestThing")
        self.test_db.cursor.execute("INSERT INTO Users (id, login, password) VALUES (?, ?, ?)",
                                    ('1', 'ManChainArgo', 'BestThing'))

    def tearDown(self):
        self.test_db.cursor.execute('DROP TABLE IF EXISTS Users')
        self.test_db.connection.commit()

    def test_success_login(self):
        result = self.test_user.do_login(self.test_db)
        self.assertTrue(result)


    def test_failure_login(self):
        self.test_failure_user = User(None,None)
        with self.assertRaises(InvalidCredentialException):
            self.test_failure_user.do_login(self.test_db)

    def test_invalid_login(self):
        self.test_failure_user = User("YouShallNot", "Pass")
        with self.assertRaises(UnknownUserException):
            self.test_failure_user.do_login(self.test_db)

    def test_invalid_password(self):
        self.test_failure_user = User("ManChainArgo", "BestTing")
        with self.assertRaises(InvalidPasswordException):
            self.test_failure_user.do_login(self.test_db)



class RegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.test_db = UsersRepository(Path(Path("testbase.db")))
        self.test_db.create_table()
        self.test_db.connection.commit()
        self.test_user = User("ManChainArgo", "BestThing")
        self.test_db.cursor.execute("INSERT INTO Users (id, login, password) VALUES (?, ?, ?)",
                                    ('1', 'ManChainArgo', 'BestThing'))

    def tearDown(self):
        self.test_db.cursor.execute('DROP TABLE IF EXISTS Users')
        self.test_db.connection.commit()



    def test_login_dublicate(self):
        with self.assertRaises(LoginExistsExeption):
            self.test_user.register(self.test_db)
        """
        self.test_user.register(self.test_db)
        self.assertRaises(LoginExistsExeption)
        """


    def test_success_register(self):
        self.test_new_user = User("TestUser", "TestPassword")
        result = self.test_new_user.register(self.test_db)
        self.assertTrue(result)
        self.test_db.cursor.execute("DELETE FROM Users WHERE login = ?", ("TestUser",))
        self.test_db.connection.commit()


    def test_password_different_layout(self):
        self.test_new_user = User("TestUser", "engрус")
        with self.assertRaises(DifferentPasswordLayoutExeption):
            self.test_new_user.register(self.test_db)

    def test_login_different_layout(self):
        self.test_new_user = User("TestUserАрбуз", "englishYO")
        with self.assertRaises(DifferentLoginLayoutExeption):
            self.test_new_user.register(self.test_db)

    def test_short_password(self):
        self.test_new_user = User("TestUser", "I")
        with self.assertRaises(ShortPasswordRegisterException):
            self.test_new_user.register(self.test_db)

    def test_too_long_password(self):
        self.test_new_user = User("TestUser", "sdfgkdsflhkdfghsfthdfghh")
        with self.assertRaises(TooLongPasswordRegisterException):
            self.test_new_user.register(self.test_db)
