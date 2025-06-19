from account import Account
import sqlite3


class Bank:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS card
                            (
                                id INTEGER PRIMARY KEY,
                                number TEXT,
                                pin TEXT,
                                balance INTEGER DEFAULT 0
                            );  
                            ''')
        self.conn.commit()

    def create_account(self):
        account = Account()
        self.cursor.execute('INSERT INTO card (number, pin, balance) VALUES (?, ?, ?)',
                            (account.identifier, account.pin, account.balance))
        self.conn.commit()

        print(f"\nYour card has been created\nYour card number:\n{account.identifier}\nYour card PIN:\n{account.pin}\n")

    def log_in_account(self):
        print("\nEnter your account number:")
        identifier = input()
        print("Enter your PIN:")
        pin = input()

        self.cursor.execute('SELECT number, pin, balance FROM card WHERE number=? AND pin=?',
                            (identifier, pin))
        result = self.cursor.fetchone()
        # print(result) # fetchone returns tuple or None

        if result:
            print("\nYou have successfully logged in!\n")
            # Load account from database
            account = Account(identifier=result[0], pin=result[1], balance=result[2])
            self.logged_in_menu(account)
        else:
            print("\nWrong card number or PIN!\n")
        return None

    def logged_in_menu(self, account):
        while True:
            print("""1. Balance
2. Log out
0. Exit""")

            # print("Select an option: ")
            usr = input()
            match usr:
                case '0':
                    print("\nBye!")
                    exit()

                case '1':
                    print(f"\nBalance: {account.get_balance()}\n")

                case '2':
                    print("\nYou have successfully logged out!\n")
                    return  # Returns to the main menu

                case _:
                    print("Invalid input!")
