# Напишите программу, которая вводит с клавиатуры непустой массив целых чисел, и
# выводит число локальных максимумов
# (элемент является локальным максимумом, если он не имеет соседей, больших, чем он сам).
my_list = [1, 4, 5, 3, 2, 6, 3, 1, 7, 8]
def search_local_max():
    local_max = 0
    if my_list[0] > my_list[1]:
        local_max += 1
    if my_list[-1] > my_list[-2]:
        local_max += 1
    for i in range(len(my_list[1:-1])):
        if my_list[i] > my_list[i-1] and my_list[i] > my_list[i + 1]:
            local_max += 1
    return local_max


print(search_local_max())

