# bank_operations.py
class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            raise ValueError("Insufficient funds. Withdrawal unsuccessful.")

    def get_balance(self):
        return self.balance


class Transaction:
    @staticmethod
    def transfer(sender, receiver, amount):
        if amount <= sender.get_balance():
            sender.withdraw(amount)
            receiver.deposit(amount)
            print(f"Transfer of ${amount} from {sender.account_holder} to {receiver.account_holder} successful.")
        else:
            print("Transfer unsuccessful. Insufficient funds in the sender's account.")
