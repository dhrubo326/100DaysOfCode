my_list = [1, 2, 3, 4]


def multyply_by2(item):
    return item * 2


new_list_created_by_map = list(map(multyply_by2, my_list))
print(new_list_created_by_map)
print(my_list)
