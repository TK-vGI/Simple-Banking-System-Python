import random


class Account:
    def __init__(self, identifier=None, pin=None, balance=0):
        self.identifier = identifier or self._generate_identifier()
        self.pin = pin or self._generate_pin()
        self.balance = balance

    def __str__(self):
        return f"Account(number={self.identifier}, balance={self.balance})"

    @staticmethod
    def _generate_identifier():
        while True:
            iin = '400000'
            ain = ''.join(str(random.randint(0, 9)) for _ in range(9))
            partial_identifier = iin + ain

            def luhn_algorithm(identifier):
                digits = [int(d) for d in identifier]  # Convert to integer list
                for i in range(0, len(digits), 2):  # Double odd-positioned digits (0-based indices 0, 2, ..., 14)
                    digits[i] *= 2
                    if digits[i] > 9:
                        digits[i] -= 9
                checksum = (10 - sum(digits) % 10) % 10
                return str(checksum)

            checksum = luhn_algorithm(partial_identifier)
            return partial_identifier + checksum

    @staticmethod
    def _generate_pin():
        return ''.join(str(random.randint(0, 9)) for _ in range(4))

    def get_balance(self, cursor=None):
        if cursor:
            cursor.execute(
                "SELECT balance FROM card WHERE number = ?",
                (self.identifier,)
            )
            result = cursor.fetchone()
            if result:
                self.balance = result[0]
        return self.balance

    def deposit(self, amount, cursor=None, conn=None):
        if amount > 0:
            self.balance += amount
            if cursor and conn:
                cursor.execute(
                    "UPDATE card SET balance = ? WHERE number = ?",
                    (self.balance, self.identifier)
                )
                conn.commit()
            # print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            raise ValueError("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid amount.")
