# coding=utf-8
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу
matrix = [[0 for _ in range(5)] for _ in range(4)]

for i in range(4):
    summ = 0
    for j in range(4):
        matrix[i][j] = int(input('Введите элемент [{}][{}]'.format(i, j)))
        summ += matrix[i][j]
    matrix[i][4] = summ

for row in matrix:
    print row
