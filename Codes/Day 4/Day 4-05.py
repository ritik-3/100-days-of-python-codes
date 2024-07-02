import random
from unicodedata import name

#test_seed = int(input("create a seed number: "))
#random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
count = len(names)
random_integer = random.randint(0, count - 1 )
print(names[random_integer])



#print(names)