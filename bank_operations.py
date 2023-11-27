# bank_operations.py
class Account:
    def __init__(self, account_holder, initial_balance, account_type="Current", interest_rate=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit of ${amount}")
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal of ${amount}")
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            raise ValueError("Insufficient funds. Withdrawal unsuccessful.")

    def get_balance(self):
        return self.balance

    def get_account_type(self):
        return self.account_type

    def add_transaction_history(self, transaction):
        self.transaction_history.append(transaction)

    def get_transaction_history(self):
        return self.transaction_history

    def set_interest_rate(self, rate):
        if self.account_type == "Savings":
            self.interest_rate = rate
            print(f"Interest rate set to {rate}% for {self.account_holder}'s Savings account.")
        else:
            print("Interest rate is only applicable to Savings accounts.")

    def calculate_interest(self):
        if self.account_type == "Savings":
            interest_amount = (self.balance * self.interest_rate) / 100
            self.balance += interest_amount
            self.transaction_history.append(f"Interest of ${interest_amount} added.")
            print(f"Interest of ${interest_amount} added to {self.account_holder}'s Savings account.")
        else:
            print("Interest is only applicable to Savings accounts.")
