from account import Account


class Bank:
    def __init__(self):
        self.accounts = {
            '4000000000000009': Account()  # Predefined dummy account
        }
        self.accounts['4000000000000009'].pin = '0000'  # Set the PIN explicitly

    def create_account(self):
        account = Account()
        self.accounts[account.identifier] = account
        print(f"\nYour card has been created\nYour card number:\n{account.identifier}\nYour card PIN:\n{account.pin}\n")

    def log_in_account(self):
        print("\nEnter your account number:")
        identifier = input()
        print("Enter your PIN:")
        pin = input()

        if identifier in self.accounts and self.accounts[identifier].pin == pin:
            print("\nYou have successfully logged in!\n")
            self.logged_in_menu(self.accounts[identifier])
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
