 # Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


factory = {}
n = 0
s = 0
while True:
    name = input(str('Введите названия предприятия или 0 если закончили ввод предприятий:'))
    if name == '0':
        break
    profit = 0
    factory[name] = profit
    for i in range(1, 5):
        profit = float(input("Прибьль за {} квартал: ".format(i)))
        factory[name] += profit
    n += 1
    s += factory[name]

if n != 0:
    avrg = s / n
    print('*' * 50)
    print("\nСредняя прибыль: {}. \nПредприятия с прибылью равной или выше среднего:".format((avrg)))
    for key in factory:
        if factory[key] >= avrg:
            print(key)

    print("\nПредприятия с прибылью меньше среднего:")
    for key in factory:
        if factory[key] < avrg:
            print(key)
    print('*' * 50)
else:
    print('Вы не ввели данные!!!')
