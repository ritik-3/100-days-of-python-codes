#BMI calculator according o different waight

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#calculate BMI
bmi_0 = weight / height ** 2
bmi = round(bmi_0, 2)

#if else 
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
    