import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()

# Update properties of a tkinter widget / component
my_label["text"] = "New Text"
my_label.config(text="New Text")

# import turtle
# tim = turtle.Turtle()
# tim.write("Some Text", font=("Times New Roman", 80, "bold"))


# Button
def button_clicked():
    # print("I got clicked")
    # my_label["text"] = "Button got clicked"
    # my_label.config(text="Button got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()


# Entry
entry = tkinter.Entry(width=30)
# index tells tkinter which item you're referring to
entry.insert(index=tkinter.END, string="Some text to begin with")
entry.pack()
# print(input.get()) # No user input at the time this code line is executed.


# Text
text = tkinter.Text(height=5, width=30)
# Put cursor in textbox
text.focus()
# Adds some text to begin with
text.insert(index=tkinter.END, chars="Example of multi-line text entry")
# Get the current value of text in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()


# Spinbox
# Get the spinbox to print the current value by listening to a function tied to the command parameter
def spinbox_used():
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Get the scale to print the current value by listening to a function tied to the command parameter
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Check box
def checkbox_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# Variable to hold on to checked state, 0 is for OFF, 1 is ON.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbox_used)
checked_state.get() # Returns nothing at this point.
checkbutton.pack()


# Radio button
# To select only one option out of different options.
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
# The 2 radio buttons are tied to the same variable, radio_state.
radiobutton1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Define a callback function to print out the current selection in the listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", func=listbox_used)
listbox.pack()



window.mainloop()
