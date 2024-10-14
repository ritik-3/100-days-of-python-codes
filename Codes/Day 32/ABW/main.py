##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import smtplib
import random as rand

my_email = "ritik.khapre5202@gmail.com"
password = "yogljntpycqzitog"

b_days = pd.read_csv("Codes/Day 32/ABW/birthdays.csv")
now = dt.datetime.now()
today_day = now.day
today_month = now.month



# Combine day and month columns
b_days['Date'] = pd.to_datetime(b_days["year"].astype(str) + '-' + b_days['month'].astype(str) + '-' + b_days['day'].astype(str), format='%Y-%m-%d')

today_birth_day = b_days[(b_days['day'] == today_day) & (b_days['month'] == today_month)]
print(today_birth_day)

# reciver details 
reciver_mail = today_birth_day["email"][0]
reciver_name = today_birth_day["name"][0]
# print(reciver_mail,reciver_name, type(reciver_mail))

# Quote chooser 

# mail send
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=reciver_mail,
#                         msg=f"Subject:Message \n\n Working"
#                         )  