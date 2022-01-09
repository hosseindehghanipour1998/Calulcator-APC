import tkinter as tk
from PIL import Image, ImageTk
from Button import *
from BackEnd.Calculator import Calculator
from msvcrt import kbhit
from Button import myButton
import tkinter.messagebox

class myUtility:

    @staticmethod
    def printOnMonitor(monitorText, monitorPointer, space=False, clear = False, isFunction = False):
        previousText = monitorPointer.cget("text")
        newText = ""
        if isFunction==False:
            if (clear):
                monitorPointer.configure(text="")
                return
            if(space):
                newText = previousText + " " + monitorText + " "
                monitorPointer.configure(text=newText)
                return
            newText = previousText + monitorText
            monitorPointer.configure(text=newText)
            isFunctionGlobal = False

        else:
            newText = monitorText + " " + "( " + str(previousText) + " )"
            monitorPointer.configure(text=newText)
            isFunctionGlobal = True

        return isFunctionGlobal

    @staticmethod
    def Standardization(expression):
        standardized = True
        try:
            # Checking First and Last Arguments
            if expression[len(expression) - 1] == '.':
                int(expression[0]) and int(expression[len(expression) - 2])
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
            standardized = False
        return standardized

    @staticmethod
    def callCalculateFunction(monitorPointer):
        expression = monitorPointer.cget("text")
        try:
            calculator = Calculator(expression, -1)
            result = calculator.calculate()
            if result>1000000:
                scientific_notation = "{:e}".format(result)
                monitorPointer.configure(text=scientific_notation)
            else:
                monitorPointer.configure(text=result)
        except:
            tk.messagebox.showinfo(title="Error", message="Wrong Input")
            monitorPointer.configure(text='')

