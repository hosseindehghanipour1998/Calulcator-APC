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
    def callCalculateFunction(monitorPointer, isFunction = True):
        expression = monitorPointer.cget("text")
        test = list(expression.split())
        print(expression)
        print(test)
        if isFunction == False and myUtility.Standardization(expression):
            calculator = Calculator(expression, -1)
            result = calculator.calculate()
            monitorPointer.configure(text=result)

        elif isFunction == True:
            checkFunction = list(expression.split())
            if checkFunction[0] == "Sin" or checkFunction[0] == "Cos" or checkFunction[0] == "Cot" or checkFunction[0] == "Tan":
                newExp = expression[expression.find("(") + 2:expression.find(")") - 1]
                calculator = Calculator(newExp, -1)
                result = calculator.calculate() # typeIsfloat
                print(result)
                functionExp = "Function" + " " + str(checkFunction[0]).lower() + " " + str(result)
                print( "Function Passing expression: "+ functionExp)
                functionCalculator = Calculator(functionExp, -1)
                finalResult = functionCalculator.calculate()
                monitorPointer.configure(text=finalResult)
            