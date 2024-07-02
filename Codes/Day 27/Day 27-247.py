from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_lable = Label(text = "I am a Lable",font= ("Ariel", 24))
my_lable.pack()

def button_clicked():
    new_txt = input.get()
    my_lable.config(text = new_txt)
    
    return

button = Button(text= "Click Me", command=button_clicked)
button.pack()

input = Entry()
input.pack()






window.mainloop()