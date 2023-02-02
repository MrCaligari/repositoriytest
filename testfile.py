# def printsale(a):
#     print(a * 10)

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