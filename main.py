# main.py
from bank_operations import Account, Transaction
from input import get_user_input_create_account, get_user_input_transfer

if __name__ == "__main__":
    # Получаем данные от пользователя для создания банковских счетов
    account_holder1, initial_balance1 = get_user_input_create_account()
    account_holder2, initial_balance2 = get_user_input_create_account()

    # Создаем два банковских счета
    account1 = Account(account_holder1, initial_balance1)
    account2 = Account(account_holder2, initial_balance2)

    # Выводим информацию о счетах
    print(f"\n{account1.account_holder}'s account created with an initial balance of ${initial_balance1}")
    print(f"{account2.account_holder}'s account created with an initial balance of ${initial_balance2}\n")

    # Получаем данные от пользователя для транзакции
    sender_name, receiver_name, amount = get_user_input_transfer()

    # Проводим транзакцию
    sender_account = account1 if sender_name == account1.account_holder else account2
    receiver_account = account1 if receiver_name == account1.account_holder else account2
    Transaction.transfer(sender_account, receiver_account, amount)

    # Выводим баланс обоих счетов
    print(f"\n{account1.account_holder}'s balance: ${account1.get_balance()}")
    print(f"{account2.account_holder}'s balance: ${account2.get_balance()}")
