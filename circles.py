import tkinter as tk
import time
import random 

x = int(input("введи горизонтальний розмір вікна: "))
d = int(input("введи вертикальний розмір вікна: "))
window = tk.Tk()
canvas = tk.Canvas(window, width = x, height = d)
canvas.pack()
colors = ("red", "orange", "yellow", "green", "cyan", "dark blue", "purple")
while True:
    i = 0
    cx = random.randint(0, x)
    cy = random.randint(0, d)
    for n in range(150, 185, 5):
        canvas.create_oval(cx - n, cy - n, cx + n, cy + n, outline = colors[i])
        canvas.update()
        i += 1
        time.sleep(0.01)
window.mainloop()
