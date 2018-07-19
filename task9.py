# coding=utf-8
'''Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр'''

a = [1111, 1, 2, 111, 123, 99, 10, 0, 12]
max_summ = 0
curr = 0
curr_temp = 0
for i in a:
    tmp_val = 0
    curr_temp = i
    while i > 0:
        tmp_val = tmp_val + (i % 10)
        i //= 10

    if tmp_val > max_summ:
        max_summ = tmp_val
        curr = curr_temp
print('Число {} имеет максимальную сумму его цифр. Сумма его цифр равняется {}.'.format(curr, max_summ))
