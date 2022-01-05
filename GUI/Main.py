import tkinter as tk
from PIL import Image, ImageTk
from Button import *
from BackEnd\
    .Calculator import Calculator
from msvcrt import kbhit
from Button import myButton
from ScientificPage import MyScientificPage


root = tk.Tk() 

canvas = tk.Canvas(root, width=350, height=240, bg='#c2d1cf')
canvas.grid(columnspan = 4, rowspan=6) # divide the canvas into 3 invisible columns

scientificPage = MyScientificPage()
scientificPage.generatePage(root)

root.mainloop()