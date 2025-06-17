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
            partial_identifier = iin + ain

            def luhn_algorithm(identifier):
                digits = [int(d) for d in identifier]  # Convert to integer list
                for i in range(len(digits) - 1, -1, -2):  # Double every second digit from the right
                    digits[i] *= 2
                    if digits[i] > 9:
                        digits[i] -= 9
                checksum = (10 - sum(digits) % 10) % 10  # Compute checksum
                return str(checksum)

            checksum = luhn_algorithm(partial_identifier)
            return partial_identifier + checksum

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
