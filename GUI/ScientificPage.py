import tkinter as tk
from PIL import Image, ImageTk
from Button import *
from Calculator import Calculator 
from msvcrt import kbhit
from Button import myButton
from Utility import *


class MyScientificPage:
    
    
    def generatePage(self, root):
        
        # Monitor
        monitor = tk.Label(root, font=("Comic Sans MS", 15,"italic"), relief=tk.SUNKEN)
        monitor.grid(rowspan=1, columnspan = 4, column=0, row=0)
        
        
        # Keyboard
        btn_mode    = myButton(root, btnRow = 1, btnColumn = 0, btnText = "%", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("%", monitor) ) # %
        btn_CE      = myButton(root, btnRow = 1, btnColumn = 1, btnText = "CE", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("", monitor, clear=True) ) # CE
        btn_C       = myButton(root, btnRow = 1, btnColumn = 2, btnText = "C", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("", monitor) ) # C 
        btn_div     = myButton(root, btnRow = 1, btnColumn = 3, btnText = "/", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("/", monitor, space=True) ) # /
        
        btn_7       = myButton(root, btnRow = 2, btnColumn = 0, btnText = "7", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("7", monitor) ) # 7
        btn_8       = myButton(root, btnRow = 2, btnColumn = 1, btnText = "8", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("8", monitor) ) # 8
        btn_9       = myButton(root, btnRow = 2, btnColumn = 2, btnText = "9", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("9", monitor) ) # 9
        btn_x       = myButton(root, btnRow = 2, btnColumn = 3, btnText = "x", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("*", monitor, space=True) ) # x
        
        btn_4       = myButton(root, btnRow = 3, btnColumn = 0, btnText = "4", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("4", monitor) ) # 4
        btn_5       = myButton(root, btnRow = 3, btnColumn = 1, btnText = "5", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("5", monitor) ) # 5
        btn_6       = myButton(root, btnRow = 3, btnColumn = 2, btnText = "6", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("6", monitor) ) # 6
        btn_sub     = myButton(root, btnRow = 3, btnColumn = 3, btnText = "-", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("-", monitor, space=True) ) # -
        
        btn_1       = myButton(root, btnRow = 4, btnColumn = 0, btnText = "1", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("1", monitor) ) # 1
        btn_2       = myButton(root, btnRow = 4, btnColumn = 1, btnText = "2", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("2", monitor) ) # 2
        btn_3       = myButton(root, btnRow = 4, btnColumn = 2, btnText = "3", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("3", monitor) ) # 3
        btn_sum     = myButton(root, btnRow = 4, btnColumn = 3, btnText = "+", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("+", monitor, space=True) ) # +
        
        btn_pow     = myButton(root, btnRow = 5, btnColumn = 0, btnText = "^", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("^", monitor, space=True) ) # ^
        btn_0       = myButton(root, btnRow = 5, btnColumn = 1, btnText = "0", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor("0", monitor) ) # 0
        btn_dot     = myButton(root, btnRow = 5, btnColumn = 2, btnText = ".", bgColor = "#20bebe", btnAction = lambda:myUtility.printOnMonitor(".", monitor) ) # .
        btn_equ     = myButton(root, btnRow = 5, btnColumn = 3, btnText = "=", bgColor = "#20bebe", btnAction = lambda:myUtility.callCalculateFunction(monitor) ) # =
