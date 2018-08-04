import random

size = int(input('Введите размер списка:'))
array = []

while len(array) < size:
    el = random.randint(-100,100)
    if el not in array:
        array.append(el)

print('Несортированнай массив : \n{}'.format(array))

n = 1
while n < len(array):
    for i in range(len(array)-n):
        if array[i]<array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]
    n += 1

print('*'*200)
print('Отсортированнай массив : \n{}'.format(array))
