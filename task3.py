# coding=utf-8
'''Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843'''
a = int(input('Введите число:'))
current = 0
temp = 0
'''Математически'''
while a > 0:
    tempcurr = a % 10
    a //= 10
    temp = a
    while temp > 0:
        tempcurr *= 10
        temp //= 10
    current += tempcurr
print ('Реверс числа: {} '.format(current))

'''по питоньи'''

b = str(input('Введите число:'))
print('Реверс числа: {} '.format(int(b[::-1])))
