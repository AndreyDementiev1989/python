# coding=utf-8
HEX_DICT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15, '15': 'F', '14': 'E', '13': 'D', '12': 'C', '11': 'B', '10': 'A'}

a = list(input('Введите первое число:').upper())
b = list(input('Введите второе число:').upper())


def summ_hex(a, b):
    while len(a) != len(b):
        if len(a) > len(b):
            b.insert(0, '0')
        else:
            a.insert(0, '0')
    a.reverse()
    b.reverse()

    c = [0] * (len(a) + 1)

    for i in range(0, len(a)):
        spam = HEX_DICT[a[i]] + HEX_DICT[b[i]]
        c[i] += spam
        while c[i] > 15:
            c[i] = c[i] % 16
            c[i + 1] += 1
        c[i] = HEX_DICT[str(c[i])]
    if c[-1] == 0:
        c.pop()
    return c[::-1]


print('Сумма чисел равна: {}'.format(summ_hex(a, b)))

# Смог только половину