# abtraction

# from eigth_class import Person

# person = Person("Alice", 25)

# person.greet()


# import qrcode

# qr = qrcode.QRCode(
#     version=1,
#     # error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )

# qr.add_data("https://www.example.com")
# qr.make(fit=True)


# encapsulation


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
        self._proctected = True

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def get_protected_status(self):
        return f"Protected status: {self._proctected}"


class User(BankAccount):

    def __init__(self, name, balance):
        super().__init__(balance)
        self.name = name

    def get_user_balance(self):
        return f"{self.name}'s balance is {super().get_balance()}"

    def get_protected_status(self):
        return f"Protected status: {self._proctected}"

    def get_balance(self):
        return str(self.__balance) + " (Accessed through User class)"


# acc = BankAccount(100)
# acc.deposit(50)
# print(acc._proctected)
# print(acc.__balance)
# print(acc.get_balance())


# user = User("Alice", 1000)
# user.deposit(500)
# print(user.get_user_balance())
# print(user.get_protected_status())
# print(user.get_balance())


class School:

    def __init__(self, name):
        self.__name = name

    @property
    def school_name(self):
        return self.__name

    @school_name.setter
    def school_name(self, new_name):
        self.__name = new_name


school = School("Greenwood High")
print(school.school_name)


school.school_name = "Blue Ridge Academy"
print(school.school_name)


