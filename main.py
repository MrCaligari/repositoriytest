# import  testfile
# testfile.printsale()
def number(num):
    mylist = []
    prev = 0
    new = 1
    summ = 0
    while num > summ:
        summ = prev + new
        new = prev
        prev = summ
        mylist.append(summ)
    if num in mylist:
        return mylist.index(num)
    else:
        return "Такого числа нет в последовательности"

num = int(input())

print(number(num))
# Фибоначчи вывести, порядковый номер числа(например 8)

# Написать функцию, которая по входному числу рисует букву w
# Например *              *               *
#           *       *       *       *
#            *               * - если пришло число 3(через пробел, не через TAB)


# объявление функции
# объявление функции
# объявление функции
# объявление функции
# объявление функции
# объявление функции
# объявление функции
# объявление функции
# объявление функции

# объявление функции
# def is_valid_password(password):
#     cnt = 0
#     password = password.split(":")
#     if len(password) == 3:
#         cnt += 1
#     if password[0] == password[0][::-1]:
#         cnt += 1
#     total = 0
#     for i in range(1, int(password[1]) + 1):
#         if int(password[1]) % i == 0:
#             total += 1
#     if total == 2:
#         cnt += 1
#     if int(password[2]) % 2 == 0:
#         cnt += 1
#     return cnt == 4
#
# # считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))