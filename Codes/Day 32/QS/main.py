import smtplib
import datetime as dt
import pandas as pd
import random as rand
import csv



my_email = "ritik.khapre5202@gmail.com"
password = "pwgoohdbodhdhwse"

#---------------------day-------------------
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("Codes/Day 32/QS/quotes.txt") as f:
        reader = f.readlines()
        chosen_row = rand.choice(reader)
    print(chosen_row)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="rebalerok1290@gmail.com",
                            msg=f"Subject:Message \n\n {chosen_row}"
                            )  
else: 
    print("lol")

