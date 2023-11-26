# input.py
def get_user_input_create_account():
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance (default is 0): "))
    return account_holder, initial_balance

def get_user_input_transfer():
    sender_name = input("Enter sender's account holder's name: ")
    receiver_name = input("Enter receiver's account holder's name: ")
    amount = float(input("Enter transfer amount: "))
    return sender_name, receiver_name, amount
