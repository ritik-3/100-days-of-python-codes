from flask import Flask, render_template
import random 
import datetime as dt
import requests


app = Flask(__name__)

@app.route('/')
def home():
    year = dt.datetime.now().year
    your_name = "Bober"
    random_number = random.randint(1,10)
    return render_template("index.html",r_num = random_number, copy_year = year, y_name = your_name)

@app.route('/guess/<name>')
def guess(name):
    g_responce = requests.get(url=f"https://api.genderize.io?name={name}")
    g_responce.raise_for_status()
    gender = g_responce.json()["gender"]
    
    a_responce = requests.get(url=f"https://api.agify.io?name={name}")
    a_responce.raise_for_status()
    age = a_responce.json()["age"]
    
    return render_template("guess.html", y_name=name,y_gender=gender,y_age=age)

if __name__ == "__main__":
    app.run()
