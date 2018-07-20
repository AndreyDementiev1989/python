# coding=utf-8
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
from random import randint

a = [random.randint(0, 1000) for x in range(10)]
print ('До замены {} :'.format(a))

max_i = 0
min_i = 0
for i in range(len(a)):
    if a[i] > a[max_i]:
        max_i = i
    elif a[i] < a[min_i]:
        min_i = i

a[max_i], a[min_i] = a[min_i], a[max_i]
print ('После замены {} :'.format(a))
