# В данном массиве найдите наибольшую серию подряд идущих элементов, расположенных по возрастанию.
def consecutive_elements():
    my_list = [1,4,5,6,8,3,2,1,6,4,2,5,2,5,7,3]
    total = 1
    max_total = 0
    for i in range(len(my_list) - 1):
        if my_list[i + 1] > my_list[i]:
            total += 1
            if total > max_total:
                max_total = total
        elif my_list[i + 1] <= my_list[i]:
            total = 1
    return max_total

print(consecutive_elements())