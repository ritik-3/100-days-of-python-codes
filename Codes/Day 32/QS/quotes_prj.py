import datetime as dt
import pandas as pd
import random as rand
import csv




now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("Codes/Day 32/QS/quotes.txt") as f:
        reader = f.readlines()
        chosen_row = rand.choice(reader)
        print(chosen_row)
else:
    print("lol")