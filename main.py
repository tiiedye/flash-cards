from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# --------------------------- DATA FRAME ------------------------------ #
df = pandas.read_csv("./data/french_words.csv")
dict_list = df.to_dict(orient="records")

current_card = {}


# -------------------------- BTN FUNCTIONS ---------------------------- #
def flip_card():
    en_word = current_card["English"]

    canvas.itemconfig(canvas_image, image=back_card_img)
    canvas.itemconfig(language_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=f"{en_word}", fill="white")


def next_card():
    global current_card
    current_card = random.choice(dict_list)
    fr_word = current_card["French"]

    canvas.itemconfig(canvas_image, image=front_card_img)
    canvas.itemconfig(language_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=f"{fr_word}", fill="black")
    window.after(3000, func=flip_card)


def known_word():
    dict_list.remove(current_card)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("French - English Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
incorrect_img = PhotoImage(file="./images/wrong.png")
correct_img = PhotoImage(file="./images/right.png")

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(columnspan=2, column=0, row=0)

language_txt = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_txt = canvas.create_text(400, 263, text="", font=WORD_FONT)

red_btn = Button(image=incorrect_img, highlightthickness=0, command=next_card)
red_btn.grid(column=0, row=1)
green_btn = Button(image=correct_img, highlightthickness=0, command=known_word)
green_btn.grid(column=1, row=1)

# All code before mainloop
next_card()
window.mainloop()
