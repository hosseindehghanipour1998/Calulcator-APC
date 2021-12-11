import tkinter as tk
from PIL import Image, ImageTk


DEFAULT_FONT_NAME = "Comic Sans MS"
DEFAULT_FONT_SIZE = 12
DEFAULT_FONT_STYLE = "italic"

DEFAULT_WIDTH_HEIGHT = 3
class myButton:
    
    def __init__(self, father, btnRow, btnColumn, btnAction, btnText = None, rowSpan = None, columnSpan = None, btnFont = (DEFAULT_FONT_NAME,DEFAULT_FONT_SIZE,DEFAULT_FONT_STYLE), bgColor = "#000000"):
        myButton = tk.Button(father, text=btnText, font = btnFont, bg=bgColor, width = DEFAULT_WIDTH_HEIGHT, command=btnAction)
        myButton.grid(row = btnRow, column=btnColumn)
        '''
        if(rowSpan != None):
            myButton.grid(rowpan = rowSpan )
        if(columnSpan != None):
            myButton.grid(columnpan = columnSpan )
            '''



