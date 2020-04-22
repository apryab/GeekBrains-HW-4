my_list = [0, 1, 5, 3, 4, 6, 1, 3, 10, 4, 6, 3, 10, 34, 23, 67]
print('Исходный список -', my_list)
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i-1] < my_list[i]]
print('Новый список -', new_list)
