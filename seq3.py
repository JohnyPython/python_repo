# Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
# Затем он вводит элементы 2-го списка
# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
# Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
# Введите элементы 2-го списка: 2,5
# Результат: 1,3,4
#
# Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно

first_list_input = input("Enter numbers of future list separated by commas ',' : ")
first_list = list(first_list_input.replace(',', ''))
print(first_list)

second_list =[]

second_user_input = int(input('Enter quantity elements of second list: '))

for elements in range(second_user_input):
    second_list.append(input('Enter {} number: '.format(elements+1)))
print(second_list)

for i in second_list:
    first_list.remove(i)

print(first_list)
