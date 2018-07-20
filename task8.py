# coding=utf-8
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу

matrix = []

for i in range(4):
    summ = 0
    matrix.append([])
    for j in range(4):
        val = int(input('Введите элемент [{}][{}]'.format(i, j)))
        matrix[i].append(val)
        summ += matrix[i][j]
    matrix[i].append(summ)

for row in matrix:
    print row
