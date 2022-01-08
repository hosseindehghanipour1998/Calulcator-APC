import tkinter as tk
from PIL import Image, ImageTk
from Button import *
from BackEnd.Calculator import Calculator
from msvcrt import kbhit
from Button import myButton
from Utility import *


class MyScientificPage:
    
    
    def generatePage(self, root):
        
        # Monitor
        monitor = tk.Label(root, font=("Andale Mono", 15,"italic"), relief=tk.SUNKEN, width=30)
        monitor.grid(rowspan=1, columnspan = 5, column=0, row=0)

        trigonometryOptions = ['Sin', 'Cos', 'Tan', 'Cot', 'Sinh', 'Cosh']

        btn_mode    = myButton(root, btnRow = 1, btnColumn = 0, btnText = "%", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("%", monitor, space=True) ) # %
        btn_CE      = myButton(root, btnRow = 1, btnColumn = 1, btnText = "CE", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("", monitor, clear=True) ) # CE
        btn_C       = myButton(root, btnRow = 1, btnColumn = 2, btnText = "C", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("", monitor)) # C
        btn_div     = myButton(root, btnRow = 1, btnColumn = 3, btnText = "/", bgColor="#84f5e8", btnAction=lambda: myUtility.printOnMonitor("/", monitor, space=True))  # /

        btn_7       = myButton(root, btnRow = 2, btnColumn = 0, btnText = "7", bgColor = "#d3f0ec", btnAction = lambda:myUtility.printOnMonitor("7", monitor) ) # 7
        btn_8       = myButton(root, btnRow = 2, btnColumn = 1, btnText = "8", bgColor = "#d3f0ec", btnAction = lambda:myUtility.printOnMonitor("8", monitor) ) # 8
        btn_9       = myButton(root, btnRow = 2, btnColumn = 2, btnText = "9", bgColor = "#d3f0ec", btnAction = lambda:myUtility.printOnMonitor("9", monitor) ) # 9
        btn_x       = myButton(root, btnRow = 2, btnColumn = 3, btnText = "x", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("*", monitor, space=True) ) # x
        
        btn_4       = myButton(root, btnRow = 3, btnColumn = 0, btnText = "4", bgColor = "#d3f0ec", btnAction = lambda:myUtility.printOnMonitor("4", monitor) ) # 4
        btn_5       = myButton(root, btnRow = 3, btnColumn = 1, btnText = "5", bgColor = "#d3f0ec", btnAction = lambda:myUtility.printOnMonitor("5", monitor) ) # 5
        btn_6       = myButton(root, btnRow = 3, btnColumn = 2, btnText = "6", bgColor = "#d3f0ec", btnAction = lambda:myUtility.printOnMonitor("6", monitor) ) # 6
        btn_sub     = myButton(root, btnRow = 3, btnColumn = 3, btnText = "-", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("-", monitor, space=True) ) # -
        
        btn_1       = myButton(root, btnRow = 4, btnColumn = 0, btnText = "1", bgColor = "#d3f0ec", btnAction = lambda:myUtility.printOnMonitor("1", monitor) ) # 1
        btn_2       = myButton(root, btnRow = 4, btnColumn = 1, btnText = "2", bgColor = "#d3f0ec", btnAction = lambda:myUtility.printOnMonitor("2", monitor) ) # 2
        btn_3       = myButton(root, btnRow = 4, btnColumn = 2, btnText = "3", bgColor = "#d3f0ec", btnAction = lambda:myUtility.printOnMonitor("3", monitor) ) # 3
        btn_sum     = myButton(root, btnRow = 4, btnColumn = 3, btnText = "+", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("+", monitor, space=True) ) # +
        
        btn_pow     = myButton(root, btnRow = 5, btnColumn = 0, btnText = "^", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("^", monitor, space=True) ) # ^
        btn_0       = myButton(root, btnRow = 5, btnColumn = 1, btnText = "0", bgColor = "#fafafa", btnAction = lambda:myUtility.printOnMonitor("0", monitor) ) # 0
        btn_dot     = myButton(root, btnRow = 5, btnColumn = 2, btnText = ".", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor(".", monitor) ) # .
        btn_equ     = myButton(root, btnRow = 5, btnColumn = 3, btnText = "=", bgColor = "#00fadd", btnAction = lambda:myUtility.callCalculateFunction(monitor) ) # =

        btn_sin     = myButton(root, btnRow = 5, btnColumn = 5, btnText = "Sin", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("Sin", monitor, isFunction=True) ) # sin
        btn_cos     = myButton(root, btnRow = 4, btnColumn = 5, btnText = "Cos", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("Cos", monitor, isFunction=True)  )# cos
        btn_cot     = myButton(root, btnRow = 3, btnColumn = 5, btnText = "Cot", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("Ctg", monitor, isFunction=True) ) # cot
        btn_tan     = myButton(root, btnRow = 2, btnColumn = 5, btnText = "Tan", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("Tan", monitor, isFunction=True) ) # tan

        btn_p_open     = myButton(root, btnRow = 5, btnColumn = 6, btnText = "(", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor("(", monitor, space=True) ) # (
        btn_p_close     = myButton(root, btnRow = 4, btnColumn = 6, btnText = ")", bgColor = "#84f5e8", btnAction = lambda:myUtility.printOnMonitor(")", monitor, space=True) ) # )
