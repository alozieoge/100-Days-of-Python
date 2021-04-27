import tkinter


def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# Update properties of a tkinter widget / component
my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button
button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
# button.place(x=0, y=0)
button.grid(column=1, row=1)

# Button 2
new_button = tkinter.Button(text="New button", command=button_clicked)
new_button.grid(column=2, row=0)


# Entry
entry = tkinter.Entry(width=30)
# index tells tkinter which item you're referring to
entry.insert(index=tkinter.END, string="Some text to begin with")
# entry.pack()
# print(input.get()) # No user input at the time this code line is executed.
entry.grid(column=3, row=2)


window.mainloop()
