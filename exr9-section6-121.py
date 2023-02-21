#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Steve", 5)
cat2 = Cat("Lilo", 7)
cat3 = Cat("fat", 3)

# 2 Create a function that finds the oldest cat

def find_oldest(cat_list):
    '''
    Function finds the oldest cat
    Input: list of cats
    Output: the oldest cat in list
    '''
    oldest_age = cat_list[0].age
    oldest_cat = cat_list[0]

    for cat in cat_list:
        if cat.age > oldest_age:
            oldest_age = cat.age
            oldest_cat = cat
    return oldest_cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {find_oldest([cat1,cat2, cat3]).age} years old.')