# coding=utf-8
# Определить, какое число в массиве встречается чаще всего
a = [1, 2, 12, 2, 2]

if len(a) == len(set(a)) != 0:
    print('Все числа разные')
elif len(a) == 0:
    print('Массив пустой')
else:
    b = {}
    count = 0
    current = None
    for i in a:
        if i not in b:
            b[i]=0
        b[i] += 1
        if  b[i] > count:
             current = i

print ('Число {} встречается чаще всего'.format(current))