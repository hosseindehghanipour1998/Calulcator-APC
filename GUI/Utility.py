import tkinter as tk
from PIL import Image, ImageTk
from Button import *
from Calculator import Calculator 
from msvcrt import kbhit
from Button import myButton
import tkinter.messagebox

class myUtility:
    
    @staticmethod
    def printOnMonitor(monitorText, monitorPointer, space=False, clear = False):
        previousText = monitorPointer.cget("text")
        newText = ""
        if(clear):
            monitorPointer.configure(text="")
            return 
        if(space):
            newText = previousText + " " + monitorText + " "
            monitorPointer.configure(text=newText)
            return
        newText = previousText + monitorText
        monitorPointer.configure(text=newText)
        
        
    @staticmethod 
    def callCalculateFunction(monitorPointer):
        expression = monitorPointer.cget("text")

        for value in expression:
            print(value)
# Standardization TEMPORARELY is here just to see the output

        try:
            #Checking First and Last Arguments
            if expression[len(expression) - 1] == '.':
                int(expression[0]) and int(expression[len(expression)-2])
            else:
                int(expression[0]) and int(expression[len(expression) - 1])

            for value in expression:
                if (value != ' ') \
                        and (value != '.') \
                        and (value.isdigit() == False) \
                        and (expression[expression.index(value) + 2] != '.'):
                    int(expression[expression.index(value) + 2])

        except:
            tk.messagebox.showinfo(title="Error", message="Wrong Input")

        calculator = Calculator(expression, -1)
        result = calculator.calculate()
                
        monitorPointer.configure(text=result)
        
            