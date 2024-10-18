import unittest
from pathlib import Path


from main import Database, InvalidCredentialException, InvalidPasswordException, UnknownUserException, LoginExistsExeption, DifferentLoginLayoutExeption, DifferentPasswordLayoutExeption, ShortPasswordRegisterException, TooLongPasswordRegisterException

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.database = Database(file_path=Path("testing_data.csv"))

    def test_success_login(self):
        username = "UserTest"
        password = "PassTest"
        with self.database as db:
            result = self.database.login(username, password)
            self.assertTrue(result)

    def test_failure_login(self):
        self.assertRaises(InvalidCredentialException, self.database.login, None, None)

    def test_invalid_login(self):
        self.assertRaises(UnknownUserException)

    def test_invalid_password(self):
        self.assertRaises(InvalidPasswordException)


class RegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.database = Database(file_path=Path("testing_data.csv"))

    def test_login_dublicate(self):
        self.assertRaises(LoginExistsExeption)

    def test_success_register(self):
        username = "admin"
        password = "1234567"
        with self.database as db:
            result = self.database.register(username, password)
            self.assertTrue(result)


    def test_password_different_layout(self):
        self.assertRaises(DifferentPasswordLayoutExeption)

    def test_login_different_layout(self):
        self.assertRaises(DifferentLoginLayoutExeption)

    def test_short_password(self):
        self.assertRaises(ShortPasswordRegisterException)

    def test_too_long_password(self):
        self.assertRaises(TooLongPasswordRegisterException)



