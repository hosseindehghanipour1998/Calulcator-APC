import tkinter as tk
from PIL import Image, ImageTk


DEFAULT_FONT_NAME = "َAndale Mono"
DEFAULT_FONT_SIZE = 15
DEFAULT_FONT_STYLE = ""

DEFAULT_WIDTH = 7
DEFAULT_HIGHT = 1
class myButton:

    def __init__(self, father, btnRow, btnColumn, btnAction, btnText = None, rowSpan = None, columnSpan = None, btnFont = (DEFAULT_FONT_NAME,DEFAULT_FONT_SIZE,DEFAULT_FONT_STYLE), bgColor = "#000000"):
        myButton = tk.Button(father, text=btnText, font = btnFont, bg=bgColor, width = DEFAULT_WIDTH, height = DEFAULT_HIGHT, command=btnAction)
        myButton.grid(row = btnRow, column=btnColumn, padx= 0, pady= 0)
        myButton.bind("<Enter>", lambda x: myButton.config(bg="#4f63f7"))
        myButton.bind("<Leave>", lambda x: myButton.config(bg="#c7cceb"))





