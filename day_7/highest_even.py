def highest_even(list):
    highest = 0
    for li_item in list:
        if li_item % 2 == 0:
            if li_item > highest:
                highest = li_item
    return highest


print(highest_even([12, 2, 4, 5, 6, 11, 10]))


def my_fun():
    pass


def test():
    pass
