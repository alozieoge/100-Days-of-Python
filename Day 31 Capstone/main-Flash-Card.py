from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
data_to_learn = {}
current_card = {}

# Read data from CSV file
try:
    data = pd.read_csv("data/words_to_learn.csv")
    print(data)
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_to_learn = original_data.to_dict(orient="records")
else:
    # Return the DataFrame as list of dictionaries:
    # [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'} ...
    data_to_learn = data.to_dict(orient="records")



def generate_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_to_learn)

    canvas.itemconfig(tagOrId=card_title, text="French", fill="black")
    canvas.itemconfig(tagOrId=card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(tagOrId=card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(tagOrId=card_title, text="English", fill="white")
    canvas.itemconfig(tagOrId=card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(tagOrId=card_background, image=card_back_img)


def word_is_known():
    data_to_learn.remove(current_card)

    new_data = pd.DataFrame(data_to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    generate_next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 30, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=generate_next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=word_is_known)
known_button.grid(row=1, column=1)

generate_next_card()


window.mainloop()

