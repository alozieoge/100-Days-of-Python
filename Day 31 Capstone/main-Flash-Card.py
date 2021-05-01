from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Read data from CSV file
data = pd.read_csv("data/french_words.csv")

# Return the DataFrame as list of dictionaries:
# [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'} ...
data_to_learn = data.to_dict(orient="records")


def generate_next_card():
    current_card = random.choice(data_to_learn)
    print(current_card)
    canvas.itemconfig(tagOrId=card_title, text="French")
    canvas.itemconfig(tagOrId=card_word, text=current_card["French"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 30, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=generate_next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=generate_next_card)
known_button.grid(row=1, column=1)

generate_next_card()


window.mainloop()

