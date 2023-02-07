# import  testfile
# testfile.printsale()
# def number(num):
#     mylist = []
#     prev = 0
#     new = 1
#     summ = 0
#     while num > summ:
#         summ = prev + new
#         new = prev
#         prev = summ
#         mylist.append(summ)
#     if num in mylist:
#         return mylist.index(num)
#     else:
#         return "Такого числа нет в последовательности"
#
# num = int(input())
#
# print(number(num))
# Фибоначчи вывести, порядковый номер числа(например 8)
import random
# Написать функцию, которая по входному числу рисует букву w
# Например *              *               *
#           *       *       *       *
#            *               * - если пришло число 3(через пробел, не через TAB)


# from random import *
# r = randint(1, 100)
# count = 0
# while True:
#     count += 1
#     n = input()
#     if n.isdigit() and int(n) > r:
#         print("Ваше число больше загаданного")
#     elif n.isdigit() and int(n) < r:
#         print("Ваше число меньше загаданного")
#     elif n.isdigit() and int(n) == r:
#         print("Вы угадали с", count, "попытки!")
#         print("Введите число еще раз!")
#     else:
#         print("Введите число заново")

# class dogs:
#     fur = True
#     paw_count = 4
#     tail = 1
#
# colly = dogs()
# print(colly.fur)
# sharik = dogs()
# print(sharik.fur)


# class cars:
#     speed = 0
#     kolesa = 4
#     def voice(self):
#         print("beep")
#
#
# ford = cars()
# print(ford.kolesa)
#
# mazda = cars()
# print(mazda.kolesa)
#
# volkswagen = cars()
# print(volkswagen.kolesa)
#
# mercedes = cars()
# print(mercedes.kolesa)
#
# mazda.voice()
# mercedes.voice()
#
# mazda.morespeed()

# from random import *
# answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
# print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
# print("Введи свое имя")
# name = input()
# print("Привет,", name)
# while True:
#     print("Задайте Ваш вопрос шару")
#     ques = input()
#     print(choice(answers))
#     print("Хотите ли Вы задать еще один вопрос? Ответьте Да или Нет")
#     ques2 = input()
#     if ques2 == "Да" or ques2 == "да":
#         continue
#     elif ques2 == "Нет" or ques2 == "нет":
#         print("Возвращайся, если возникнут вопросы!")
#         break
#     else:
#         print("Введите Да или Нет")

# from random import *
# digits = '0123456789'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# punctuation = '!#$%&*+-=?@^_'
# chars = ''
# print("Сколько паролей необходимо сгенерировать?")
# much = int(input())
# print("Длина пароля")
# length = int(input())
# print("Включать ли цифры 0123456789?")
# isdigits = input()
# print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?")
# isuppercase = input()
# print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?")
# islowercase = input()
# print("Включать ли символы !#$%&*+-=?@^_?")
# issymbols = input()
# while True:
#     if isdigits.lower() == "да":
#         chars += digits
#     else:
#         input("Ответьте да или нет")
#     if isuppercase == "да":
#         chars += uppercase_letters
#     else:
#         input("Ответьте да или нет")
#     if islowercase == "да":
#         chars += lowercase_letters
#     else:
#         input("Ответьте да или нет")
#     if issymbols == "да":
#         chars += punctuation
#     break

# def generate_password(chars, length):
#     return sample(chars, length)
#
#
# for i in range(int(much)):
#     print(*generate_password(chars, length), sep="")

# def number(num):
#     mylist = []
#     prev = 0
#     new = 1
#     summ = 0
#     for i in range(num):
#         summ = prev + new
#         new = prev
#         prev = summ
#     return new
#
# print(number(int(input())))

# def get_w(num):
#     l_space = 0
#     r_space = num + 2
#     w_list = []
#     string = ""
#     for i in range(num):
#         if i == 0:
#             string = (l_space * " " + "*" + r_space * " " + "*" + r_space * " ")
#         elif i == num - 1:
#             string = (l_space * " " + "*" + l_space * " ")
#         else:
#             string = (l_space * " " + "*" + r_space * " " + "*" + r_space * " ")
#         w_list.append(string)
#         l_space += 1
#         r_space -= 2
#     for i in range(num):
#         print(w_list[i])
#
# get_w(int(input()))

from random import *

# def number(num):
#     mylist = [0, 1]
#     for i in range(num):
#         mylist.append(mylist[i] + mylist[i + 1])
#     return mylist[i + 1]
#
# print(number(int(input())))


def get_w(num):
    w_list = []
    string = ""
    for i in range(num):
        if i == 0:
            string = "*" + (num * 2 - 2) * " " + "*" + (num * 2 - 2) * " " + "*"
        elif i == num - 1:
            string = ((num - 1) * " " + "*") + ((num - 1) * 2 * " " + "*")
        else:
            string = (i * " " + "*" + (num -1 - i) * " " + "*")
        w_list.append(string)
    for i in range(num):
        print(w_list[i])

    print(w_list, end="\n")

get_w(int(input()))
