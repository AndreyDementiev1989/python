# coding=utf-8
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать
a = [1, 2, 2, 10, 3, 4, 2]

max = a[0]
min = a[0]
min_i = 0
max_i = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_i = i
    elif a[i] < min:
        min = a[i]
        min_i = i

if min_i > max_i:
    min_i, max_i = max_i, min_i
print(sum(a[min_i + 1:max_i]))
