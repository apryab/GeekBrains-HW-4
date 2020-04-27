def check_unique(my_var, my_list):
    i = 0
    for elem in my_list:
        if elem == my_var:
            i += 1
    if i == 1:
        return 1
    else:
        return 0


init_list = [0, 1, 2, 3, 4, 5, 1, 4, 3]
new_list = [el for el in init_list if check_unique(el, init_list) == 1]
print('Исходный список:', init_list)
print('Список элементов без повторений:', new_list)
