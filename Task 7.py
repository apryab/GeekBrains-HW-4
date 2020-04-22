from math import factorial


def fibo_gen():
    for el in range(1, 16):
        fact = factorial(el)
        yield fact


my_list = [el for el in fibo_gen()]
print('Нужный список:', my_list)
