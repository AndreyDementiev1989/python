# -*- coding: utf-8 -*-
'''В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
'''
a = range(2, 100)
b = {x: 0 for x in range(2, 10)}
for i in b.keys():
    for j in a:
        if j % i == 0:
            b[i] += 1
    print('Кратных {} : {}'.format(i, b[i]))
