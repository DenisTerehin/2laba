import numpy as np

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def display(self):
        for row in self.matrix:
            print(row)

    def _check_dimensions(self, other, operation):
        if operation == "сложение матриц" and (self.rows != other.rows or self.cols != other.cols):
            raise ValueError(f"Невозможно выполнить {operation}. Размеры матриц не совпадают.")

    def _validate_element(self, element):
        if not isinstance(element, (int, float)):
            raise ValueError("Элемент матрицы должен быть числом (int или float).")

    def set_element(self, i, j, value):
        self._validate_element(value)
        self.matrix[i][j] = value

class MatrixOperations:
    @staticmethod
    def add_matrices(matrix1, matrix2):
        matrix1._check_dimensions(matrix2, "сложение матриц")
        result = Matrix(matrix1.rows, matrix1.cols)
        for i in range(matrix1.rows):
            for j in range(matrix1.cols):
                result.matrix[i][j] = matrix1.matrix[i][j] + matrix2.matrix[i][j]
        return result

    @staticmethod
    def multiply_matrices(matrix1, matrix2):
        matrix1._check_dimensions(matrix2, "умножение матриц")

        result = Matrix(matrix1.rows, matrix2.cols)
        for i in range(matrix1.rows):
            for j in range(matrix2.cols):
                for k in range(matrix1.cols):
                    result.matrix[i][j] += matrix1.matrix[i][k] * matrix2.matrix[k][j]
        return result

    @staticmethod
    def scalar_multiply(matrix, scalar):
        result = Matrix(matrix.rows, matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.matrix[i][j] = matrix.matrix[i][j] * scalar
        return result

    @staticmethod
    def transpose_matrix(matrix):
        result = Matrix(matrix.cols, matrix.rows)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.matrix[j][i] = matrix.matrix[i][j]
        return result

    @staticmethod
    def determinant(matrix):
        if matrix.rows != matrix.cols:
            raise ValueError("Определитель определен только для квадратных матриц")
        return np.linalg.det(matrix.matrix)

    @staticmethod
    def inverse_matrix(matrix):
        if matrix.rows != matrix.cols:
            raise ValueError("Обратная матрица определена только для квадратных матриц")
        if np.linalg.det(matrix.matrix) == 0:
            raise ValueError("Обратная матрица не существует, так как определитель равен нулю")

        inv_matrix = Matrix(matrix.rows, matrix.cols)
        inv_matrix.matrix = np.linalg.inv(matrix.matrix).tolist()
        return inv_matrix
