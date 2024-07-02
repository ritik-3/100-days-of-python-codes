#Find out how many days, weeks, years you have left
age_0 = input("What is your current age?")
age = int(age_0)
days = age * 365
weeks = age * 52
years = age 

#total for 90
total_days = 90 * 365
total_weeks = 90 * 52
total_years = 90

#days left
days_left = total_days - days
weeks_left = total_weeks - weeks
years_left = total_years - years

message = (f"you have {days_left} days, {weeks_left} weeks and {years_left} years left.")
print(message)