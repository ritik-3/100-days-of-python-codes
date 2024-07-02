#coffie machine project

#here the menu

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 25,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 75,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

PROFIT = 0

#function for resource repot 
def resource_report():
    print(f"Amount or water is {resources['water']}. ")
    print(f"Amount of milk is {resources['milk']}. ")
    print(f"Amount of coffee is {resources['coffee']}. ")

#function for resources check
def check_resources(needed_ingredients):
    for item in needed_ingredients:
        if needed_ingredients[item] > resources[item]:
            print(f"Sorry, the resources are not enough. ")
            return False
    return True

#funciton for transaction 
def transaction():
    print("please insert money")
    total = 0
    total += int(input("How many notes of 50: ")) * 50
    total += int(input("How many notes of 20: ")) * 20
    total += int(input("How many notes of 10: ")) * 10
    total += int(input("How many notes of 5: ")) * 5
    return total
    
#function for making coffee
def make_coffee(drink_name, other_ingredients):
    for item in other_ingredients:
        resources[item] -+ other_ingredients[item]
    print(f"Here's your {drink_name}, Enjoy. ")
        

#function for verifying purchase 
def verify_purchase(total_amount, needed_amount):
    if total_amount >= needed_amount:
        change = total_amount - needed_amount
        print(f"Here's your change {change}. ")
        global PROFIT
        PROFIT += needed_amount
        return True 
    else:
        print("Sorry the given ammount is not enouch to make the purchase. ")
        return False
        

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False

    elif choice == "report":
        resource_report()
        
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = transaction()
            if verify_purchase(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
            