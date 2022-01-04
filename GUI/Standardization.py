import tkinter as tk
from PIL import Image, ImageTk
from Button import *
from Calculator import Calculator
from msvcrt import kbhit
from Button import myButton
from Utility import *

class standardization:

    @staticmethod
    def checkText(expression):
        try:
            if expression[len(expression) - 1] == '.':
                int(expression[0]) and int(expression[len(expression) - 2])
            else:
                int(expression[0]) and int(expression[len(expression) - 1])

            for value in expression:
                if value != ' ' and value != '.' and value.isdigit() == False:
                    if expression[expression.index(value) + 2] != '.':
                        int(expression[expression.index(value) + 2])

        except:
            tk.messagebox.showinfo(title="Error", message="Wrong Input")




