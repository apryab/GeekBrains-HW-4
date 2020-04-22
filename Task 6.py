from itertools import count
from itertools import cycle


def unit_generator(var1, var2):
    for el in count(var1):
        print(el)
        if el == var2:
            break
    return


def list_iterator(my_list, my_amount):
    i = 0
    for el in cycle(my_list):
        if i == my_amount:
            break
        print(el)
        i += 1
    return


init_list = [1, 2, 7, 10, 4, 100, 35, 3, 1, 1, 26, 25, 24, 26, 100, 1, 101, 0, 3, 3, 3]
while True:
    print('Каким итератором вы хотели бы воспользоваться?')
    print('1 - Итератор по целым числам, начиная с заданного')
    print('2 - Итератор по заданному изначально списку')
    choice = input()
    try:
        choice = int(choice)
        if (choice == 1) or (choice == 2):
            break
        else:
            print('Введите один из пунктов меню')
    except(TypeError, ValueError):
        print('Нужно ввести число')
if choice == 1:
    while True:
        start = input('Введите число, с которого вы бы хотели начать ')
        end = input('И число, которым хотите закончить ')
        try:
            start = int(start)
            end = int(end)
            if start < end:
                break
            else:
                print('Начало должно быть меньше конца')
        except(ValueError, TypeError):
            print('Надо ввести целые числа')
    unit_generator(start, end)
if choice == 2:
    while True:
        amount = input('Введите, сколько чисел вы хотели бы получить ')
        try:
            amount = int(amount)
            break
        except(ValueError, TypeError):
            print('Надо ввести целое положительное число ')
    list_iterator(init_list, amount)
