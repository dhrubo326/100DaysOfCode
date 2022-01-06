my_list = [2, 4, 6, 7]

print(list(map(lambda item: item**2, my_list)))


a = [(0, 2), (4, 3), (9, 9), (10, -1)]

# Normal process for sort

# def get_key(item):
# 	return item[1]
# print(sorted(a, key=get_key))

# sort tuple using lambda
a.sort(key=lambda item: item[1])
# print(list(filter(lambda item: item[1], a)))
print(a)