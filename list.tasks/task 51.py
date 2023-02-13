# В данном массиве найдите два наименьших элемента.
def check_min_value():
    my_list = [1,4,5,2,6,10,7,82,6,3]
    my_list.sort()
    print(*my_list[:2])


check_min_value()
