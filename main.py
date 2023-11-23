# main.py
from calculator_operations import Calculator

def main():
    # Создаем экземпляр калькулятора
    calculator = Calculator()

    # Вводим числа
    num1 = float(input("Введите первое1 число: "))
    num2 = float(input("Введите второе число: "))

    # Выбираем операцию
    operation = input("Выберите операцию (+, -, *): ")

    # Выполняем операцию и выводим результат
    if operation == '+':
        result = calculator.add(num1, num2)
        print(f"Результат сложения: {result}")
    elif operation == '-':
        result = calculator.subtract(num1, num2)
        print(f"Результат вычитания: {result}")
    elif operation == '*':
        result = calculator.multiply(num1, num2)
        print(f"Результат умножения: {result}")
    else:
        print("Некорректная операция. Пожалуйста, выберите +, - или *.")

if __name__ == "__main__":
    main()
