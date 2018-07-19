'''Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
 Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке'''

'''Через enumerate'''

for i, ch in enumerate(range(32, 128)):
    print('{} - {}, '.format(ch, chr(ch)), end=' ')
    if (i + 1) % 10 == 0:
        print('\n')

print('\n')

'''Без enumerate'''
j = 1
for i in range(32, 128):
    print('{} - {}, '.format(i, chr(i)), end=' ')
    if j % 10 == 0:
        print('\n')
    j += 1
