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

    print(w_list, sep="\n")

get_w(int(input()))