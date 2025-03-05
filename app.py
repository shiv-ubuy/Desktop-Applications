import tkinter as tk
from tkinter import Canvas

def on_click():
    print("Jai Hind!")

# Create main window
root = tk.Tk()
root.title("India Flag Button")

# Create a button with the Indian flag design
canvas = Canvas(root, width=300, height=180)
canvas.pack()

# Draw the flag
canvas.create_rectangle(10, 10, 290, 70, fill="orange", outline="black")  # Saffron
canvas.create_rectangle(10, 70, 290, 130, fill="white", outline="black")  # White
canvas.create_rectangle(10, 130, 290, 190, fill="green", outline="black")  # Green

# Draw the Ashoka Chakra
chakra = canvas.create_oval(120, 75, 180, 135, outline="blue", width=2)
for i in range(24):
    angle = (i * 15) * (3.14159 / 180)
    x1 = 150 + 15 * (3.14159 / 180) * (3.14159 - angle)
    y1 = 105 + 15 * (3.14159 / 180) * (3.14159 - angle)
    x2 = 150 + 35 * (3.14159 / 180) * (3.14159 - angle)
    y2 = 105 + 35 * (3.14159 / 180) * (3.14159 - angle)
    canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

# Create a button with the flag
button = tk.Button(root, text="Jai Hind!", command=on_click, font=("Arial", 12, "bold"))
button_window = canvas.create_window(150, 210, window=button)

root.mainloop()
