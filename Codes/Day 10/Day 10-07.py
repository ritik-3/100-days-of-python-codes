#calculatar 
import art
#add
def add(n1, n2):
    return n1 + n2

#substract
def substract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "/": divide,
    "*": multiply,
}
print(art.logo)
def calculator():
    num1 = float(input("What's the first number?:"))
    for keys in operations:
            print(keys)
    if_contionue = True
    while if_contionue:
        operation_symbol = input("Pick an operation from line above")
        num2 = float(input("What's the next number"))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        cont = input("Type 'y' if you want to continue and type 'n' if you want to reset the calculator ")
        if cont == "y":
            if_contionue = True
            num1 = answer 
            
        elif cont == "n":
            if_contionue = False 
            calculator()
            
calculator()