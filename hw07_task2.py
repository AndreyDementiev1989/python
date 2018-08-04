import random

size = int(input('Введите размер списка:'))
array = []

while len(array) < size:
    el = random.uniform(0,50)
    if el not in array:
        array.append(el)
print('Несортированнай массив : \n{}'.format(array))


def merge_sort(array):

    if len(array)<=1:
        return array
    mid = int(len(array)/2)
    left = merge_sort(array[mid:])
    rigth = merge_sort(array[:mid])
    return merge(left,rigth)
def merge(left, rigth) :
    result = []
    while len(left)>0 and len(rigth) >0:
        if left[0] <= rigth[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(rigth[0])
            rigth = rigth[1:]
    if len(left) > 0:
        result += left
    if len(rigth)>0:
        result += rigth
    return result



print('Отсортированнай массив : \n{}'.format(merge_sort(array)))