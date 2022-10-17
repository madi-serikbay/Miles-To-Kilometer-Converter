from tkinter import *


def miles_to_km():
    miles = int(miles_input.get())
    km = 1.609 * miles
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


# Label1
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)



# Label2
mile_label = Label(text="Mile")
mile_label.grid(column=2, row=0)



# Label3
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)


# Label4
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)


# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


# Entry1
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)



window.mainloop()