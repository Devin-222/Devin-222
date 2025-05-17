import tkinter as tk
import random

# Flip function
def flip_coin():
    result = random.choice(["Heads", "Tails"])
    result_label.config(text=result)

# Set up GUI window
window = tk.Tk()
window.title("Coin Flip")
window.geometry("300x200")

# Title Label
title_label = tk.Label(window, text="Flip the Coin!", font=("Arial", 18))
title_label.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 24), fg="blue")
result_label.pack(pady=20)

# Flip Button
flip_button = tk.Button(window, text="Flip", font=("Arial", 14), command=flip_coin)
flip_button.pack()

# Run the GUI loop
window.mainloop()
