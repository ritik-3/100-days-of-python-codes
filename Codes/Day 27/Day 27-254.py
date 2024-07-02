from tkinter import *


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


my_label = Label(text="is eqal to", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=2)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

my_label = Label(text="miles", font=("Arial", 24, "bold"))
my_label.grid(column=3, row=0)

km_result = Label(text= "0")
km_result.grid(column= 1, row= 2)


my_label = Label(text="KM", font=("Arial", 24, "bold"))
my_label.grid(column=3, row=2)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)


window.mainloop()