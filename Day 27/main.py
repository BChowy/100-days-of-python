from tkinter import *


def convert_miles_to_km():
    mile = num_of_miles.get()
    result = float(mile) * 1.609
    num_of_km.config(text=result)


window = Tk()
window.title("Mile to Km Converter")
window.maxsize(400, 200)
window.minsize(400, 200)
window.config(padx="100", pady="50")

num_of_miles = Entry(width=10)
num_of_miles.config(justify="center")
num_of_miles.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(padx="10", pady="10")

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

num_of_km = Label(text="0")
num_of_km.grid(column=1, row=1)
num_of_km.config(pady="10")

km = Label(text="Km")
km.grid(column=2, row=1)

calc = Button(text="Calculate", command=convert_miles_to_km)
calc.grid(column=1, row=2)


window.mainloop()
