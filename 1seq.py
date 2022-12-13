
num_count = int(input('Количество цифр: ')) # спрашиваем количесвто чисел

my_list = [] # создаем пустой список
for i in range(num_count): # запрашиваем числа по очереди
    num = int(input(f'Введите число({i+1}): '))
    my_list.append(num)

my_list.sort() # сортируем список

print(my_list) # вывод