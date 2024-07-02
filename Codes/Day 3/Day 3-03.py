#Check if the number is even or odd
number = int(input("Which number do you want to check? "))

#modular code
modulas = number % 2

#if else code
if modulas == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")