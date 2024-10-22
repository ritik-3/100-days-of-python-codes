from flask import Flask

def make_bold(func):
    def wrapper_function():
        return f"<b>{func()}</b>"
    return wrapper_function

def make_emphasise(func):
    def wrapper_function():
        return f"<em>{func()}</em>"
    return wrapper_function

def make_underline(func):
    def wrapper_function():
        return f"<u>{func()}</u>"
    return wrapper_function

app = Flask(__name__)


@app.route("/")
@make_bold
@make_emphasise
@make_underline
def hello():
    return "<h1 style='text-align: center'>This is Kurba Bober!!</h1>" \
           "<p style='text-align: center'>Bober from Futur</p>" \
           "<div style='text-align: center'> \
           <img src ='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2l1d29meDVqanY3MGU5M2V2Y3A1c2U2dnhjd3B2MTFwZmt6NW1oMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cpkjiJfwjHO7bWBp90/giphy.gif'>\
               </div>"


if __name__ == "__main__":
    app.run(debug=True)