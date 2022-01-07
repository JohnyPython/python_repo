# Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться
# никакими библиотеками кроме random)
# Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока
# использовать строку
# Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
# Пример использования sample:
# import random
# numbers = [1, 2, 3, 4, 5]
#
# # 2 - количество случайных элементов
# result = random.sample(numbers, 2)
#
# print(result) # [5, 1]
#
# После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
# пользователь вводит дату в формате 'dd.mm.yyyy'
#
# Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде:
# третье января 2009 года, склонением можно пренебречь
#
# В конце считаем количество правильных и неправильных ответов и предлагаем начать снова

import random


while True:
    famous_peoples = {'Ilon Mask': '28.06.1971', 'Sergei Brin': '21.08.1973', 'Jack Ma': '10.09.1964',
                      'Bruce Lee': '20.07.1940', 'Guido van Rossum': '31.01.1956', 'Magnus Carlsen': '30.11.1990',
                      'Maria Skłodowska-Curie': '07.11.1867', 'Martin Scorsese': '17.11.1942',
                      'Evgeny Kharlamov': '11.06.1985', 'Ekaterina Kharlamova': '11.10.1983'}

    famous_peoples_keys_list = list(famous_peoples.keys())

    random_five_names = random.sample(famous_peoples_keys_list, 5)
    right_answer_count = 0
    wrong_answer_count = 0
    for i in random_five_names:
        input_birthday = input("Enter {}'s birthday(dd.mm.yyyy): ".format(i))
        if famous_peoples[i] == input_birthday:
            right_answer_count += 1
        else:
            wrong_answer_count += 1
            print('Wrong answer, birthday of {} : {}'.format(i, famous_peoples[i]))

    print("Right answers: {}".format(right_answer_count))
    print("Wrong answers: {}".format(wrong_answer_count))

    ask_about_play = input('Do you want play again?(yes/no): ')
    if ask_about_play == 'no':
        print('Давай до свиданья!!!')
        break

