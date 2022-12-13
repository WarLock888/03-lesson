
s = input('Введите список через запятую(точку с запятой, слэш): ')

if ',' in s: # разделитель запятая
    my_list = s.split(',')
elif ';' in s: # разделитель точка с запятой
    my_list = s.split(';')
else: # разделитель остался только слэш
    my_list = s.split('/')

print('Исходный список:', my_list)

uniq_list = list(set(my_list))
print('Уникальный список:', uniq_list)






