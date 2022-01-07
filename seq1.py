# Задание:
# Пользователь вводит количество элементов будущего списка
# После этого по очереди по одной вводит любые цифры
# Сохранить цифры в список
# Отсортировать список по возрастанию и вывести на экран
# Пример работы: Введите количество элементов: 3
# Введите 1 элемент: 5
# Введите 2 элемент: 2
# Введите 3 элемент: 4
# Вывод: [2, 4, 5]

new_list = []
user_input = int(input('Enter number of items in the new list: '))
for i in range(user_input):
    new_list.append(int(input("Enter {} number: ".format(i + 1))))
    new_list.sort()

print('Output :', new_list)
