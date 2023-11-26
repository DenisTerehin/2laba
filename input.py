def get_account_info():
    account_number = input("Enter your account number: ")
    initial_balance = float(input("Enter your initial balance: "))
    return account_number, initial_balance


def get_deposit_amount():
    return float(input("Enter the deposit amount: "))


def get_withdrawal_amount():
    return float(input("Enter the withdrawal amount: "))


def get_menu_choice():
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Account Information")
    print("4. Exit")
    return input("Enter your choice (1-4): ")
