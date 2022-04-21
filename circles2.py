import tkinter as tk
import random
import time

wid = int(input("Enter width of window: "))
hei = int(input("Enter height of window: "))
maxr = int(input("Enter maximun radius of balls: "))
minr = 5
maxspeed = int(input("Enter max speed of balls: "))
nb = int(input("Enter number of balls: "))
w = tk.Tk()
canv = tk.Canvas(w, width = wid, height = hei)
canv.pack()
circles = []
colors = ("black", "brown", "red", "orange", "yellow", "green", "cyan", "dark blue", "purple", "grey20")
for i in range(0, nb):
    r = random.randint(minr, maxr)
    cx = random.randint(r, wid - r)
    cy = random.randint(r, hei - r)
    fillcolor = random.choice(colors)
    outcolor = random.choice(colors)
    oval = canv.create_oval(cx - r, cy - r, cx + r, cy + r, fill = fillcolor, outline = outcolor)
    dx = random.randint(-1 * maxspeed, maxspeed)
    dy = random.randint(-1 * maxspeed, maxspeed)
    circles.append({"dx": dx, "dy": dy, "id": oval})
while True:
    for circle in circles:
        coor = canv.coords(circle['id'])
        if coor[0] < 0 or coor[2] > wid:
            circle["dx"] *= -1
        if coor[1] < 0 or coor[3] > hei:
            circle["dy"] *= -1
        canv.move(circle["id"], circle["dx"], circle["dy"])
    canv.update()
    time.sleep(0.005) 
w.mainloop()  
