import tkinter as tk
from PIL import Image, ImageTk
from Button import *
from Calculator import Calculator 
from msvcrt import kbhit
from Button import myButton

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
        
        calculator = Calculator(expression, -1)
        result = calculator.calculate()
        
        monitorPointer.configure(text=result)
        
            