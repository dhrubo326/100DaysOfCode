
# Comprehensions exercise
some_list = ['a', 'b', 'c', 'c', 'd', 'n', 'p', 'n']


duplicates = list(set([item for item in some_list if some_list.count(item) > 1 ]))

print(duplicates) 