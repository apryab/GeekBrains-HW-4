from sys import argv

script_name, param1, param2, param3 = argv
try:
    param1 = float(param1)
    param2 = float(param2)
    param3 = float(param3)
    print('Считаем зарплату сотрудника')
    salary = (param1 * param2) + param3
    print('Зарплата составила:', salary)
except(ValueError, TypeError):
    print('Вы ввели не числа!')
