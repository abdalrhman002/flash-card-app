import tkinter as ttk
import pandas as pd
import random

random_row_of_data = {}
data_to_learn = {}

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_to_learn = pd.read_csv("data/french_words.csv")
    data_list = data_to_learn.to_dict(orient="records")
else:
    data_list = data.to_dict(orient="records")


def next_word():
    global random_row_of_data, flib_timer
    window.after_cancel(flib_timer)
    random_row_of_data = random.choice(data_list)
    canvas.itemconfig(card_word, text=random_row_of_data["French"], fill="black")
    canvas.itemconfig(card_tittle, text="French", fill="black")
    canvas.itemconfig(card_img, image=front_img)
    flib_timer = window.after(3000, flib_card)


def flib_card():
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(card_tittle, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_row_of_data["English"], fill="white")


def i_know_this_word():
    data_list.remove(random_row_of_data)
    new_data = pd.DataFrame(data_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    print(len(data_list))
    next_word()


window = ttk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flib_timer = window.after(3000, flib_card)

canvas = ttk.Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = ttk.PhotoImage(file="images/card_front.png")
back_img = ttk.PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 233, image=front_img)
card_tittle = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

next_word()

correct_img = ttk.PhotoImage(file="images/right.png")
correct_button = ttk.Button(image=correct_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=i_know_this_word)
correct_button.grid(row=1, column=1)

wrong_img = ttk.PhotoImage(file="images/wrong.png")
wrong_button = ttk.Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)


window.mainloop()
