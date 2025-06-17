import random


class Account:
    def __init__(self):
        self.identifier = self._generate_identifier()
        self.pin = self._generate_pin()
        self.balance = 0

    @staticmethod
    def _generate_identifier():
        while True:
            iin = '400000'
            ain = ''.join(str(random.randint(0, 9)) for _ in range(9))
            checksum = '9'
            return iin + ain + checksum

    @staticmethod
    def _generate_pin():
        return ''.join(str(random.randint(0, 9)) for _ in range(4))

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")