#tip calculator using python
from unittest import result


print("welcome to tip calculator")
total_0 = input("What was the total bill?")
tip_input_0 = input("what percentage of tip would you like to give 10, 12 or 15")

tip_input_1 = int(tip_input_0)
total_1 = int(total_0)
#calculate tip
tip_input_2 = tip_input_1 / 100
tip_percentage = tip_input_2 * total_1

#add tip
total = total_1 + tip_percentage

#divide
people_0 = input("How many peoples to split the bill?")
people = int(people_0)

#result
result = total / people
print(round(result), 2)