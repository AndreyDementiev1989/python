# coding=utf-8
# Найти максимальный элемент среди минимальных элементов столбцов матрицы
import random
from random import randint
matrix = [[random.randint(0,22) for _ in range(3)] for _ in range(3)]
for line in matrix:
    print(line)

current = None

for j in range(len((matrix)[0])):
    spam = matrix[0][j]
    for i in range(len(matrix)):
        if spam > matrix[i][j]:
           spam = matrix[i][j]
    if current is None:
        current = spam
    else:
        if current < spam:
            current = spam

print (current)




