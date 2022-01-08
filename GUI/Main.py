import tkinter as tk
from PIL import Image, ImageTk
from Button import *
from BackEnd\
    .Calculator import Calculator
from msvcrt import kbhit
from Button import myButton
from ScientificPage import MyScientificPage


root = tk.Tk()

root.resizable(0, 0)
root.title("VUB Rostam Scientific Calculator")
root.iconphoto(False, tk.PhotoImage(file='vub.png'))

canvas = tk.Canvas(root, width=550, height=245, bg='#c2d1cf')
canvas.grid(columnspan = 7, rowspan=6)

scientificPage = MyScientificPage()
scientificPage.generatePage(root)

root.mainloop()