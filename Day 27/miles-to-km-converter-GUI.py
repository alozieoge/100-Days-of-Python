import tkinter


def miles_to_km(miles):
    return round(miles * 1.60934, 2)


def button_clicked():
    miles = float(miles_entry.get())
    km = miles_to_km(miles)
    km_result_label.config(text=str(km))


window = tkinter.Tk()
window.title(string="Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=20)

miles_entry = tkinter.Entry(width=15)
miles_entry.insert(index=tkinter.END, string="0")
miles_entry.grid(column=1, row=0)

miles_unit_label = tkinter.Label(text="Miles")
# miles_unit_label["text"] = "Miles"
miles_unit_label.config(padx=10, pady=10)
miles_unit_label.grid(column=2, row=0)

equal_to_label = tkinter.Label(text="is equal to")
# equal_to_label["text"] = "is equal to"
equal_to_label.grid(column=0, row=1)

km_result_label = tkinter.Label(text="0")
km_result_label.grid(column=1, row=1)

km_unit_label = tkinter.Label(text="Km")
# km_unit_label["text"] = "Km"
km_unit_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=button_clicked)
# calculate_button.config(text="Calculate")
calculate_button.grid(column=1, row=2)

window.mainloop()


