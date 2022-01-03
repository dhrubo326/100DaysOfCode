my_list = [1, 2, 3, 4, 5]


def only_odd(item):
    return item % 2 != 0


new_list_created_by_filter = list(filter(only_odd, my_list))
print(new_list_created_by_filter)
print(my_list)