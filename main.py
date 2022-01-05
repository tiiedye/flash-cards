from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("French - English Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
incorrect_img = PhotoImage(file="./images/wrong.png")
correct_img = PhotoImage(file="./images/right.png")

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas .create_image(400, 265, image=front_card_img)
canvas.grid(columnspan=2, column=0, row=0)

language_txt = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
word_txt = canvas.create_text(400, 263, text="word here", font=WORD_FONT)

red_btn = Button(image=incorrect_img, highlightthickness=0)
red_btn.grid(column=0, row=1)
green_btn = Button(image=correct_img, highlightthickness=0)
green_btn.grid(column=1, row=1)

# All code before mainloop
window.mainloop()
