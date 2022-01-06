# модуль 5
# Пользователь вводит любые цифры через запятую
# Сохранить цифры в список
# Получить новый список в котором будут только уникальные элементы исходного
# (уникальным считается символ, который встречается в исходном списке только 1 раз)
# Вывести новый список на экран
# Порядок цифр в новом списке не важен
# Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
# Результат: 2, 4, 6, 9
#
# (Дополнительно*) Предусмотреть что пользователь может использовать один из 3-х разделителей: запятую, точку с запятой,
# слэш (1,2,3 1;2;3 1/2/3), но только какой то один 1,2;3/4 - так нельзя


user_input = input("Enter numbers separated by commas ',' : ")
user_input = list(user_input.replace(',', ''))
unique_list = list(set(user_input))
print(','.join(unique_list))
