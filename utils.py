from input import get_account_info, get_deposit_amount, get_withdrawal_amount, get_menu_choice


class Transaction:
    def __init__(self, transaction_id, description, amount):
        self.transaction_id = transaction_id
        self.description = description
        self.amount = amount

    def display_transaction_info(self):
        print(f"Transaction {self.transaction_id}: {self.description}, Amount: {self.amount}")


class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = {}

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction_id = len(self.transactions) + 1
            transaction = Transaction(transaction_id, "Deposit", amount)
            self.transactions[transaction_id] = transaction
            print(f"Deposited {amount} into account {self.account_number}.")
        else:
            print("Invalid deposit amount. Amount should be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            transaction_id = len(self.transactions) + 1
            transaction = Transaction(transaction_id, "Withdrawal", amount)
            self.transactions[transaction_id] = transaction
            print(f"Withdrew {amount} from account {self.account_number}.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Amount should be greater than 0.")
        else:
            print("Insufficient funds for withdrawal.")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")
        print("Transaction History:")
        for transaction in self.transactions.values():
            transaction.display_transaction_info()



if __name__ == "__main__":
    # Получаем данные от пользователя
    account_number, initial_balance = get_account_info()

    # Создаем экземпляр счета
    account = Account(account_number, initial_balance)

    while True:
        choice = get_menu_choice()

        if choice == "1":
            deposit_amount = get_deposit_amount()
            account.deposit(deposit_amount)
        elif choice == "2":
            withdrawal_amount = get_withdrawal_amount()
            account.withdraw(withdrawal_amount)
        elif choice == "3":
            account.display_account_info()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
