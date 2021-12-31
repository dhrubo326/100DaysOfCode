class Pets():
    animals = []  # do not found any use of it.

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walking())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walking(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1 Add nother Cat


class Mini(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
cat1 = Simon('simon', 5)
cat2 = Sally('Sally', 9)
cat3 = Mini('Mini', 15)
my_cats = [cat1, cat2, cat3]
# print(cat2.walk2())

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()
