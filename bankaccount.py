class BankAccount:
    """Класс представления банковского счета"""
    def __init__(self, balance:int):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount:int):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def close(self):
        self._balance = 0








# код для проверки
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0