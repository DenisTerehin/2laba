from matrix import Matrix, MatrixOperations

def get_matrix_from_input():
    try:
        rows = int(input("Введите количество строк матрицы: "))
        cols = int(input("Введите количество столбцов матрицы: "))
        
        if rows <= 0 or cols <= 0:
            raise ValueError("Количество строк и столбцов должно быть больше нуля.")
        
        matrix = Matrix(rows, cols)
        print("Введите элементы матрицы:")

        for i in range(rows):
            row_input = input(f"Введите элементы {i + 1}-й строки через пробел: ")
            row_values = list(map(int, row_input.split()))

            if len(row_values) != cols:
                raise ValueError("Неверное количество элементов в строке.")

            matrix.matrix[i] = row_values

        return matrix

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return get_matrix_from_input()

def choose_operation():
    print("\nВыберите операцию:")
    print("1. Сложение матриц")
    print("2. Умножение матриц")
    print("3. Умножение матрицы на скаляр")
    print("4. Транспонирование матрицы")
    print("5. Вычисление определителя матрицы")
    print("6. Вычисление обратной матрицы")
    print("0. Завершить программу")
    
    try:
        choice = int(input("Введите номер операции (0-6): "))
        if choice not in range(0, 7):
            raise ValueError("Введите число от 0 до 6.")
        return choice
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return choose_operation()

def main():
    matrix1 = get_matrix_from_input()

    while True:
        matrix2 = get_matrix_from_input()
        
        # Проверка на возможность умножения матриц
        while matrix1.cols != matrix2.rows:
            print("Невозможно умножить матрицы: количество столбцов первой матрицы не равно количеству строк второй матрицы.")
            matrix2 = get_matrix_from_input()

        operation = choose_operation()

        if operation == 0:
            print("Программа завершена.")
            break

        if operation == 1:
            result = MatrixOperations.add_matrices(matrix1, matrix2)
        elif operation == 2:
            result = MatrixOperations.multiply_matrices(matrix1, matrix2)
        elif operation == 3:
            try:
                scalar = int(input("Введите скаляр: "))
            except ValueError as e:
                print(f"Ошибка ввода: {e}")
                continue
            result = MatrixOperations.scalar_multiply(matrix1, scalar)
        elif operation == 4:
            result = MatrixOperations.transpose_matrix(matrix1)
        elif operation == 5:
            result = MatrixOperations.determinant(matrix1)
        elif operation == 6:
            result = MatrixOperations.inverse_matrix(matrix1)
        else:
            print("Неверный выбор операции.")
            continue

        print("\nРезультат:")
        if isinstance(result, Matrix):
            result.display()
        else:
            print(result)

        matrix1 = result  # Используем полученную матрицу как новую для следующей операции

if __name__ == "__main__":
    main()

