from bank import Bank

def main():
    bank = Bank() # Create an instance of Bank
    # Menu
    while True:
        print("""1. Create an account
2. Log into account
0. Exit""")

        # User input
        usr = input()
        match usr:
            case '0':
                print("\nBye!")
                break

            case '1':
                bank.create_account()

            case '2':
                bank.log_in_account()

            case _:
                print('Invalid input!\n')



if __name__ == '__main__':
    main()
