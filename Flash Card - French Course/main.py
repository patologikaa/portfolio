
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pandas.read_csv("./data/5000_french_words.csv")
    to_learn = orginal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_item, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_item, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    generate_word()
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)

window = Tk()
window.title("Flash Card = French Course")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)

canvas = Canvas(height=526, width=800)
card_front_image=PhotoImage(file="./images/card_front.png")
card_back_image=PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_image)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400,150, text= "Title", font=("Ariel", 40, "italic"))
card_item = canvas.create_text(400,263, text= "word", font=("Ariel", 40, "bold"))


right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

generate_word()
window.mainloop()