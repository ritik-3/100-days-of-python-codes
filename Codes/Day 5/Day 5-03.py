# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(", ")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_hight = 0
for hight in student_heights:
    total_hight += hight
#print(total_hight)

no_of_students = 0
for student in student_heights:
  no_of_students += 1
  average_hight = round(total_hight / no_of_students)
print(average_hight)