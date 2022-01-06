# SET comprehensions
my_list1 = {cha for cha in 'sabit sihab'}
print(my_list1)
my_list4 = {num**2 for num in range(0, 50) if num % 2 != 0}
print(my_list4)


# Dictionary comprehensions

my_dict = {
    'a': 2,
    'b': 3,
    'c': 4
}
output_dict = {key: item**2 for key, item in my_dict.items() if item % 2 == 0}
print(output_dict)

dict2 = {num:num*2 for num in [1, 2, 3]}
print(dict2)
