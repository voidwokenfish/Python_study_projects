import datetime
class User:
    def __init__(self, email, nickname, password, age):
        self.email = email
        self.nickname = nickname
        self.password = password
        self.age = age

    def __lt__(self, other):
        return self.email.lower() < other.email.lower()

    @staticmethod
    def register():
        email = input("Введите почту: ")
        if email.endswith("@gmail.com"):
            Users.checker(email, "email")

        else:
            print("Почта введена некорректно, попробуйте еще раз.")
            User.register()
        nickname = input("Придумайте ник: ")
        Users.checker(nickname, "nickname")
        password = input("Придумайте пароль: ")
        age = input("Введите дату рождения в формате dd.mm.yyyy: ")
        Users.checker(age, "age")

        with open("user_data.txt", "a") as filus:
            filus.write(f'{email}:{nickname}:{password}:{age}')
        gigasort("user_data.txt")


class Users:
    def __init__(self):
        self.users_list = []

    def add_user_in_users_list(self, user: User):
        self.users_list.append(user)
        self.users_list.sort()

    def binary_search(self, target, type):
        gigasort("user_data.txt")
        if not self.users_list:
            self.lister()
        high = len(self.users_list) - 1
        low = 0
        mid = 0
        if type == "email":
            while low <= high:
                mid = (low + high) // 2
                if self.users_list[mid].email.lower() == target.lower():
                    return self.users_list[mid]
                elif self.users_list[mid].email.lower() > target.lower():
                    high = mid - 1
                else:
                    low = mid + 1
            return None
        elif type == "nickname":
            while low <= high:
                mid = (low + high) // 2
                if self.users_list[mid].nickname.lower() == target.lower():
                    return self.users_list[mid]
                elif self.users_list[mid].nickname.lower() > target.lower():
                    high = mid - 1
                else:
                    low = mid + 1
            return None

    @staticmethod
    def checker(data, checker_type):
        with open("user_data.txt", "r") as checklist:
            checklist_rdlns = checklist.readlines()
            for line in checklist_rdlns:
                split_checklist = line.split(":")
                if checker_type == "email":
                    if data == split_checklist[0]:
                        print("Эта почта уже есть в базе")
                        return User.register()
                elif checker_type == "nickname":
                    if data == split_checklist[1]:
                        print("Этот ник занят")
                        return User.register()
                elif checker_type == "age":
                    try:
                        age_date = datetime.datetime.strptime(data, "%d.%m.%Y")
                    except ValueError:
                        print("Неверный формат даты")
                        User.register()

    @staticmethod
    def lister():
        with open("user_data.txt", "r") as file:
            list_with_users = file.readlines()
        for line in list_with_users:
            user_info_list = line.split(':')
            email = user_info_list[0]
            nickname = user_info_list[1]
            password = user_info_list[2]
            age = user_info_list[3]
            our_users.add_user_in_users_list(User(email, nickname, password, age))

def gigasort(file_name):
    with open(file_name, "r") as file:
        readlined = file.readlines()
    sorted_file = sorted(readlined, key=lambda x: x.split(":")[0].lower())
    with open(file_name, "w") as file:
        for line in sorted_file:
            file.write(line.strip() + "\n")

def menu():
    our_users.lister()
    gigasort("user_data.txt")
    print("1)Узнать данные об аккаунте\n2)Зарегистрировать")
    choice = input("Выберите действие: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            choice_2 = input("1)Узнать данные через почту\n2)Узнать данные по нику\n")
            if int(choice_2) == 1:
                arg = input("Введите почту: ")
                user = our_users.binary_search(arg, "email")
                if user:
                    print(f'Данные о пользователе {arg}:\n'
                          f'Ник - {user.nickname}\n'
                          f'Почта - {user.email}\n'
                          f'Дата рождения - {user.age}')
            if int(choice_2) == 2:
                arg = input("Введите ник: ")
                user = our_users.binary_search(arg, "nickname")
                if user:
                    print(f'Данные о пользователе {arg}:\n'
                          f'Ник - {user.nickname}\n'
                          f'Почта - {user.email}\n'
                          f'Дата рождения - {user.age}')
        elif choice == 2:
            return User.register()
        else:
            print("Некорректный ввод")
            menu()
    else:
        print("Некорректный ввод")
        menu()


our_users = Users()
menu()
