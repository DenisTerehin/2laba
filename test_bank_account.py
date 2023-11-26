import unittest
from unittest.mock import patch, call
from utils import Account, Transaction
from input import get_account_info, get_deposit_amount, get_withdrawal_amount, get_menu_choice

class TestAccount(unittest.TestCase):

    def test_deposit(self):
        account = Account("123456", 1000)
        account.deposit(500)
        self.assertEqual(account.balance, 1500)

    def test_withdraw(self):
        account = Account("123456", 1000)
        account.withdraw(300)
        self.assertEqual(account.balance, 700)

    def test_invalid_withdrawal(self):
        account = Account("123456", 1000)
        account.withdraw(1200)
        self.assertEqual(account.balance, 1000)

    def test_invalid_deposit(self):
        account = Account("123456", 1000)
        account.deposit(-200)
        self.assertEqual(account.balance, 1000)

    def test_display_account_info(self):
        account = Account("123456", 1000)
        expected_output = [
            "Account Number: 123456",
            "Current Balance: 1000",
            "Transaction History:"
        ]
        with patch('builtins.print') as mock_print:
            account.display_account_info()

            # Получаем все вызовы print
            actual_calls = [call(args[0]) for args, _ in mock_print.call_args_list]

            # Проверяем, что каждая строка ожидаемого вывода присутствует в вызовах
            for output_line in expected_output:
                self.assertIn(call(output_line), actual_calls)

            # Проверяем, что количество вызовов совпадает с ожидаемым
            self.assertEqual(len(actual_calls), len(expected_output))

class TestUserInput(unittest.TestCase):

    @patch('builtins.input', side_effect=["JohnDoe", "1500"])
    def test_get_account_info(self, mock_input):
        account_number, initial_balance = get_account_info()
        self.assertEqual(account_number, "JohnDoe")
        self.assertEqual(initial_balance, 1500)

    @patch('builtins.input', return_value="500")
    def test_get_deposit_amount(self, mock_input):
        deposit_amount = get_deposit_amount()
        self.assertEqual(deposit_amount, 500)

    @patch('builtins.input', return_value="300")
    def test_get_withdrawal_amount(self, mock_input):
        withdrawal_amount = get_withdrawal_amount()
        self.assertEqual(withdrawal_amount, 300)

    @patch('builtins.input', return_value="2")
    def test_get_menu_choice(self, mock_input):
        menu_choice = get_menu_choice()
        self.assertEqual(menu_choice, "2")

if __name__ == '__main__':
    unittest.main()
