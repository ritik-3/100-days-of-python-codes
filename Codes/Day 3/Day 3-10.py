#Love Calculator
from itertools import count
from re import U


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#lowring cases
name_1 = name1.lower() 
name_2 = name2.lower()

#count
t = (name_1 + name_2).count("t")
r = (name_1 + name_2).count("r")
u = (name_1 + name_2).count("u")
e = (name_1 + name_2).count("e")
total_1 = (t + r + u + e)

l = (name_1 + name_2).count("l")
o = (name_1 + name_2).count("o")
v = (name_1 + name_2).count("v")
e = (name_1 + name_2).count("e")
total_2 = (l + o + v + e )

total = int(str(total_1) + str(total_2))

if (total < 10) or (total > 90):
    print(f"Your score is {total}%, you go together like coke and mentos.")
elif (total > 40) or (total < 50):
    print(f"Your score is {total}%, you are alright together.")
else:
    print(f"Your score is {total}%.")