# Определите, есть ли в массиве повторяющиеся элементы.
def check_replay_elements():
    my_list = [1,4,5,2,"Привет","Пока",7.5,3,4]
    for i in my_list:
        total = my_list.count(i)
        if total >= 2:
            return "YES"
    else:
        return "NO"
print(check_replay_elements())

