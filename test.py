import tkinter as tk
import random
import time
from tkinter import messagebox

def start_game():
    global score, game_running
    score = 0
    game_running = True
    update_score_label()
    root.after(game_duration * 1000, end_game)
    randomly_populate_moles()

def end_game():
    global game_running
    game_running = False
    tk.messagebox.showinfo("Game Over", f"Game Over! Your final score is {score}")
    reset_moles()

def randomly_populate_moles():
    if game_running:
        for mole_button in mole_buttons:
            mole_button["state"] = tk.NORMAL
            mole_button["text"] = ""
            root.after(random.randint(1000, 3000), lambda button=mole_button: show_mole(button))

def show_mole(button):
    time = 1000 # time mole is showen for (ms)
    if game_running:
        button["text"] = "Mole"
        button["state"] = tk.NORMAL
        root.after(time, lambda b=button: hide_mole(b))

def hide_mole(button):
    if game_running:
        button["text"] = ""
        button["state"] = tk.DISABLED
        root.after(random.randint(1000, 3000), lambda b=button: show_mole(b))

def whack_mole(row, col):
    if game_running:
        button = mole_buttons[row * 3 + col]
        if button["text"] == "Mole":
            global score
            score += 1
            update_score_label()
            hide_mole(button)

def update_score_label():
    score_label["text"] = f"Score: {score}"

def reset_moles():
    for mole_button in mole_buttons:
        mole_button["text"] = ""
        mole_button["state"] = tk.DISABLED

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Game 3")

    score = 0
    game_running = False
    game_duration = 20  # in seconds

    mole_buttons = []

    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text="Mole", width=10, height=3, command=lambda r=row, c=col: whack_mole(r, c))
            button.grid(row=row, column=col)
            mole_buttons.append(button)

    start_button = tk.Button(root, text="Start", command=start_game)
    start_button.grid(row=3, column=0, columnspan=3)

    score_label = tk.Label(root, text="Score: 0")
    score_label.grid(row=4, column=0, columnspan=3)

    root.mainloop()
