# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

matrix = [[1, 2, 3], [4, 5, 6]]


def transposed_matrix(matrix):
    return list(zip(matrix[0], matrix[1]))


print(transposed_matrix(matrix))
