from flask import Flask

app = Flask(__name__)

@app.route('/')

@app.route('/<name>,')
def greeting(name):
    return f'hello there {name}, you are 21 years old.'

if __name__ == '__main__':
    app.run(debug=True)