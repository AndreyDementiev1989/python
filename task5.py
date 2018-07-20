# coding=utf-8
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
from random import randint

a = [random.randint(-30, 30) for _ in range(20)]
print (a)
current_i = -1
i = 0
while i < len(a):
    if a[i] < 0 and current_i == -1:
        current_i = i
    elif a[i] < 0 and a[i] > a[current_i]:
        current_i = i
    i += 1

if current_i != -1:
    print('Число {} с индексом  {}'.format(a[current_i], current_i))
else:
    print('Нет отрицательных элементов')
