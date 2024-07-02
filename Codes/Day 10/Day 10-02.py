#Function for formating Name in right order.

def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You didn't provide valid input"
    f_result = f_name.title()
    l_result = l_name.title()
    return f"Result: {f_result} {l_result}"
    
    
formated_f_name = input("Write your first name: \n")
formated_l_name = input("Write your last name; \n")

print(format_name(f_name= formated_f_name , l_name = formated_l_name))
    