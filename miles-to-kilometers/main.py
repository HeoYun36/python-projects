from tkinter import *


def calculate_mile_to_km():
    mile = input_miles.get()
    km_result = 1.609 * float(mile)
    result.config(text=f"{km_result}")


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

input_miles = Entry(width=10)
input_miles.insert(END, string="0")
input_miles.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km = Label(text="km")
km.grid(column=2, row=1)

calculate = Button(text="Calculate", command=calculate_mile_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
