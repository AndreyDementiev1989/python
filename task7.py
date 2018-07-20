# coding=utf-8
# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться

a = [4, 0, 3, 4, 2, 2, 1, 1, -3]
if len(a) == 0 or len(a) == 1:
    print('Неверный размер массива')
else:
    if a[0] > a[1]:
        min_one = 0
        min_two = 1
    else:
        min_one = 1
        min_two = 0

    for i in range(2, len(a)):
        if a[i] < a[min_one]:
            spam = min_one
            min_one = i
            if a[spam] < a[min_two]:
                min_two = spam
        elif a[i] < a[min_two]:
            min_two = i

print('Первое минимальное {} имеет индекс {}'.format(a[min_one], min_one + 1))
print('Второе минимальное {} имеет индекс {}'.format(a[min_two], min_two + 1))
