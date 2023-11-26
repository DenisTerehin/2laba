import unittest
from unittest.mock import patch
from bank_operations import Account, Transaction
from input import get_user_input_create_account, get_user_input_transfer

class TestBankApp(unittest.TestCase):
    def setUp(self):
        self.account1 = Account("Alice", 1000)
        self.account2 = Account("Bob", 500)

    def test_account_deposit(self):
        self.account1.deposit(200)
        self.assertEqual(self.account1.get_balance(), 1200)

    def test_account_withdrawal_sufficient_funds(self):
        self.account1.withdraw(200)
        self.assertEqual(self.account1.get_balance(), 800)

    def test_account_withdrawal_insufficient_funds(self):
        with patch('bank_operations.Account.withdraw', side_effect=Exception("Insufficient funds")):
            with self.assertRaises(Exception) as context:
                self.account1.withdraw(200)
            self.assertEqual(str(context.exception), "Insufficient funds")

        # Verify that the balance remains the same
        self.assertEqual(self.account1.get_balance(), 1000)

    def test_transaction_successful(self):
        Transaction.transfer(self.account1, self.account2, 200)
        self.assertEqual(self.account1.get_balance(), 800)
        self.assertEqual(self.account2.get_balance(), 700)

    def test_transaction_insufficient_funds(self):
        with patch('bank_operations.Account.withdraw', side_effect=Exception("Insufficient funds")):
            with self.assertRaises(Exception) as context:
                Transaction.transfer(self.account1, self.account2, 200)
            self.assertEqual(str(context.exception), "Insufficient funds")

        # Verify that the balances remain the same
        self.assertEqual(self.account1.get_balance(), 1000)
        self.assertEqual(self.account2.get_balance(), 500)

    def test_integration_create_account_and_transfer(self):
        with patch('builtins.input', side_effect=['Charlie', '0', 'Alice', 'Charlie', '100']):  # Use side_effect
            account_holder, initial_balance = get_user_input_create_account()
            new_account = Account(account_holder, initial_balance)

            Transaction.transfer(self.account1, new_account, 50)
            self.assertEqual(self.account1.get_balance(), 950)
            self.assertEqual(new_account.get_balance(), 50)

if __name__ == '__main__':
    unittest.main()
