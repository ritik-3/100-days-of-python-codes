import random

test_seed = int(input("create a seed number: "))
random.seed(test_seed)

random_integer = random.randint(0, 1)

if random_integer == 0:
    print("Head")
else:
    print("Tails")
