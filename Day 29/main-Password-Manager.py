import tkinter
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, tkinter.END)
    password_entry.insert(index=0, string=password)

    # Copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if website_text == "" or password_text == "":
        messagebox.showerror(title="Error", message="Please make sure there are no empty fields.")
    else:
        is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nEmail: {email_text} "
                               f"\nPassword: {password_text} \n\nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website_text} | {email_text} | {password_text}\n")

            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)  # x and y position of the centre of the image.
# canvas.pack()
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "alozie@gmail.com")

password_entry = tkinter.Entry(width=22)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
