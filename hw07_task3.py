array = [0,6,3,1,7,4,9,2,5]
print(array)

for i in range(0,len(array)):
    n = 0
    m = 0
    for j in range(0,len(array)):
        if array[i] != array[j]:
            if array[i]>array[j]:
                n += 1
            else:
                m += 1
    if m == n:
        print('Медиана это значение {} под индесом {}'.format(array[i],i))

