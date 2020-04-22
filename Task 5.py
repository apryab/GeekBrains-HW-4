from functools import reduce


def multiplier(var1, var2):
    return var1 * var2


list_even = [i for i in range(100, 1001, 2)]
multiply = reduce(multiplier, list_even)
print('Результат перемножения -', multiply)
