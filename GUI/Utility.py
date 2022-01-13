
import tkinter as tk
from PIL import Image, ImageTk
from Button import *
from BackEnd.Calculator import Calculator
from msvcrt import kbhit
from Button import myButton
import tkinter.messagebox


class myUtility:

    isEqualPushed = False

    @staticmethod
    def printOnMonitor(monitorText, monitorPointer, space=False, clear = False, isFunction = False, cIsTrue = False):
        #try:
        myOperatorList = {'+', '-', '/', '*', '^', '%'}
        monitorTextTest = monitorText

        if myUtility.isEqualPushed == True and isFunction == False and monitorTextTest not in myOperatorList:
            monitorPointer.configure(text="")

        myUtility.isEqualPushed = False

        previousText = monitorPointer.cget("text")
        if cIsTrue == False:
            newText = ""
            if isFunction==False:
                if (clear):
                    monitorPointer.configure(text="")
                    return
                if(space):
                    newText = str(previousText) + " " + str(monitorText) + " "
                    monitorPointer.configure(text=newText)
                    return
                newText = str(previousText) + str(monitorText)
                monitorPointer.configure(text=newText)
                isFunctionGlobal = False
            else:
                newText = str(monitorText) + " " + "( " + str(previousText) + " )"
                monitorPointer.configure(text=newText)
                isFunctionGlobal = True

            return isFunctionGlobal
        else:
            previousTextList = previousText.split(" ")
            previousTextList = [x for x in previousTextList if x != " " and x != '']
            if len(previousTextList) > 0:
                previousTextList.pop()
                previousText = " ".join(previousTextList) + " "
                monitorPointer.configure(text=previousText)

        '''except:
            tk.messagebox.showinfo(title="Error", message="Oops... We ran into an error, Try again!")
            monitorPointer.configure(text='')'''


    @staticmethod
    def callCalculateFunction(monitorPointer):

        myUtility.isEqualPushed = True
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
