# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
mini = Cat('mini', 5)
tusi = Cat('tusi', 7)
pusi = Cat('pusi', 12)


# 2 Create a function that finds the oldest cat
# Find the oldes cat
def find_oldest_cat(*args):
    return max(args)
 

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'the oldest cat is {find_oldest_cat(mini.age, tusi.age, pusi.age)} years old')

