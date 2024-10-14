import pandas as pd
import datetime as dt
import smtplib
import random as rand

my_email = "your mail"
password = "Your pass"

# Read birthday CSV
b_days = pd.read_csv("Codes/Day 32/ABW/birthdays.csv")
now = dt.datetime.now()
today_day = now.day
today_month = now.month

# Combine day and month columns into a single DateTime object
b_days['Date'] = pd.to_datetime(b_days["year"].astype(str) + '-' + b_days['month'].astype(str) + '-' + b_days['day'].astype(str), format='%Y-%m-%d')

# Filter today's birthdays
today_birth_day = b_days[(b_days['day'] == today_day) & (b_days['month'] == today_month)]

if not today_birth_day.empty:
    # Receiver details
    reciver_mail = today_birth_day["email"].iloc[0]
    reciver_name = today_birth_day["name"].iloc[0]
    
    # Quote chooser 
    temp_1 = "Codes/Day 32/ABW/letter_templates/letter_1.txt"
    temp_2 = "Codes/Day 32/ABW/letter_templates/letter_2.txt"
    temp_3 = "Codes/Day 32/ABW/letter_templates/letter_3.txt"

    rand_temp = rand.choice([temp_1, temp_2, temp_3])

    # Open template and replace placeholder
    with open(rand_temp, 'r') as file:
        template = file.read()

    updated_template = template.replace("[NAME]", reciver_name)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=reciver_mail,
            msg=f"Subject:Happy Birthday!\n\n{updated_template}"
        )
    print(f"Email sent to {reciver_name} ({reciver_mail})")
else:
    print("No birthdays today.")
