#Напишите функцию для транспонирования матрицы


def matrix_transposition(a):
    trans_a = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    return (trans_a)


x = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(x)
print(matrix_transposition(x))

