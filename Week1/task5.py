class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # приватний атрибут

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Створення об’єкта
account = BankAccount(1000)

# Робота через методи класу
account.deposit(500)
account.withdraw(300)

print(account.get_balance())

# Спроба прямої зміни балансу (не працює)
account.__balance = 0
print(account.get_balance())
