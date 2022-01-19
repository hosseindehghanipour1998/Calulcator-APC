import tkinter as tk
from Button import *
from Calculator import Calculator
from Button import myButton
from Utility import *



class MyScientificPage:
    
    def generatePage(self, root, canvas):
        
        
        # Monitor
        monitor = tk.Label(root, font=("Andale Mono", 15,"italic"), relief=tk.SUNKEN, width=58)
        monitor.grid(rowspan=1, columnspan = 8, column=0, row=0)

        btn_mode = myButton(root, btnRow=1, btnColumn=0, btnText="⌈x⌉", bgColor="#3F4CFF", btnAction=lambda: myUtility.printOnMonitor("Ceil", monitor, isFunction=True))  # ceil
        btn_CE = myButton(root, btnRow=2, btnColumn=0, btnText="⌊x⌋", bgColor="#3F4CFF", btnAction=lambda: myUtility.printOnMonitor("Floor", monitor, isFunction=True))  # floor
        btn_div = myButton(root, btnRow=3, btnColumn=0, btnText="|x|", bgColor="#3F4CFF", btnAction=lambda: myUtility.printOnMonitor("Exp", monitor, isFunction=True))  # exp
        btn_C = myButton(root, btnRow=4, btnColumn=0, btnText="√", bgColor="#3F4CFF", btnAction=lambda: myUtility.printOnMonitor("Sqrt", monitor, isFunction=True))  # sqrt
        btn_div = myButton(root, btnRow=5, btnColumn=0, btnText="Log", bgColor="#3F4CFF", btnAction=lambda: myUtility.printOnMonitor("Log", monitor, isFunction=True))  # log

        btn_mode    = myButton(root, btnRow = 1, btnColumn = 1, btnText = "%", bgColor = "#3F4CFF", btnAction = lambda:myUtility.printOnMonitor("%", monitor, space=True) ) # %
        btn_CE      = myButton(root, btnRow = 1, btnColumn = 2, btnText = "CE", bgColor = "#3F4CFF", btnAction = lambda:myUtility.printOnMonitor("", monitor, clear=True) ) # CE
        btn_C       = myButton(root, btnRow = 1, btnColumn = 3, btnText = "C", bgColor = "#3F4CFF", btnAction = lambda:myUtility.printOnMonitor("", monitor, cIsTrue=True)) # C
        btn_div     = myButton(root, btnRow = 1, btnColumn = 4, btnText = "/", bgColor="#3F4CFF", btnAction=lambda: myUtility.printOnMonitor("/", monitor, space=True))  # /

        btn_7       = myButton(root, btnRow = 2, btnColumn = 1, btnText = "7", bgColor = "#6EAFF4", btnAction = lambda:myUtility.printOnMonitor("7", monitor) ) # 7
        btn_8       = myButton(root, btnRow = 2, btnColumn = 2, btnText = "8", bgColor = "#6EAFF4", btnAction = lambda:myUtility.printOnMonitor("8", monitor) ) # 8
        btn_9       = myButton(root, btnRow = 2, btnColumn = 3, btnText = "9", bgColor = "#6EAFF4", btnAction = lambda:myUtility.printOnMonitor("9", monitor) ) # 9
        btn_x       = myButton(root, btnRow = 2, btnColumn = 4, btnText = "x", bgColor = "#3F4CFF", btnAction = lambda:myUtility.printOnMonitor("*", monitor, space=True) ) # x
        
        btn_4       = myButton(root, btnRow = 3, btnColumn = 1, btnText = "4", bgColor = "#6EAFF4", btnAction = lambda:myUtility.printOnMonitor("4", monitor) ) # 4
        btn_5       = myButton(root, btnRow = 3, btnColumn = 2, btnText = "5", bgColor = "#6EAFF4", btnAction = lambda:myUtility.printOnMonitor("5", monitor) ) # 5
        btn_6       = myButton(root, btnRow = 3, btnColumn = 3, btnText = "6", bgColor = "#6EAFF4", btnAction = lambda:myUtility.printOnMonitor("6", monitor) ) # 6
        btn_sub     = myButton(root, btnRow = 3, btnColumn = 4, btnText = "-", bgColor = "#3F4CFF", btnAction = lambda:myUtility.printOnMonitor("-", monitor, space=True) ) # -
        
        btn_1       = myButton(root, btnRow = 4, btnColumn = 1, btnText = "1", bgColor = "#6EAFF4", btnAction = lambda:myUtility.printOnMonitor("1", monitor) ) # 1
        btn_2       = myButton(root, btnRow = 4, btnColumn = 2, btnText = "2", bgColor = "#6EAFF4", btnAction = lambda:myUtility.printOnMonitor("2", monitor) ) # 2
        btn_3       = myButton(root, btnRow = 4, btnColumn = 3, btnText = "3", bgColor = "#6EAFF4", btnAction = lambda:myUtility.printOnMonitor("3", monitor) ) # 3
        btn_sum     = myButton(root, btnRow = 4, btnColumn = 4, btnText = "+", bgColor = "#3F4CFF", btnAction = lambda:myUtility.printOnMonitor("+", monitor, space=True) ) # +
        
        btn_pow     = myButton(root, btnRow = 5, btnColumn = 1, btnText = "^", bgColor = "#3F4CFF", btnAction = lambda:myUtility.printOnMonitor("^", monitor, space=True) ) # ^
        btn_0       = myButton(root, btnRow = 5, btnColumn = 2, btnText = "0", bgColor = "#6EAFF4", btnAction = lambda:myUtility.printOnMonitor("0", monitor) ) # 0
        btn_dot     = myButton(root, btnRow = 5, btnColumn = 3, btnText = ".", bgColor = "#3F4CFF", btnAction = lambda:myUtility.printOnMonitor(".", monitor) ) # .
        btn_dot     = myButton(root, btnRow = 5, btnColumn = 4, btnText = "☼ |☽",bgColor = "#3F4CFF", btnAction=lambda:myUtility.toggleDarkMode(root=root, canvas=canvas,inputLabel=monitor)) #nagative
        btn_equ     = myButton(root, btnRow = 5, btnColumn = 6, btnText = "=", bgColor = "#FF6E14", columnspan=3, btnAction = lambda:myUtility.callCalculateFunction(monitor), width=16 ) # =

        btn_sin     = myButton(root, btnRow = 2, btnColumn = 6, btnText = "Sin", bgColor = "#3F4CFF", fgColor = "#cdd1d0", btnAction = lambda:myUtility.printOnMonitor("Sin", monitor, isFunction=True) ) # sin
        btn_cos     = myButton(root, btnRow = 3, btnColumn = 6, btnText = "Cos", bgColor = "#3F4CFF", fgColor = "#cdd1d0", btnAction = lambda:myUtility.printOnMonitor("Cos", monitor, isFunction=True)  )# cos
        btn_cot     = myButton(root, btnRow = 4, btnColumn = 6, btnText = "Cot", bgColor = "#3F4CFF", fgColor = "#cdd1d0", btnAction = lambda:myUtility.printOnMonitor("Ctg", monitor, isFunction=True) ) # cot
        btn_tan     = myButton(root, btnRow = 4, btnColumn = 7, btnText = "Tan", bgColor = "#3F4CFF", fgColor = "#cdd1d0", btnAction = lambda:myUtility.printOnMonitor("Tan", monitor, isFunction=True) ) # tan

        btn_p_open     = myButton(root, btnRow = 1, btnColumn = 6, btnText = "(", bgColor = "#3F4CFF", fgColor = "#cdd1d0", btnAction = lambda:myUtility.printOnMonitor("(", monitor, space=True) ) # (
        btn_p_close     = myButton(root, btnRow = 1, btnColumn = 7, btnText = ")", bgColor = "#3F4CFF", fgColor = "#cdd1d0", btnAction = lambda:myUtility.printOnMonitor(")", monitor, space=True) ) # )
        btn_p_open = myButton(root, btnRow=2, btnColumn=7, btnText="Sinh", bgColor="#3F4CFF", fgColor = "#cdd1d0", btnAction=lambda: myUtility.printOnMonitor("Sinh", monitor, isFunction=True))  # sinh
        btn_p_close = myButton(root, btnRow=3, btnColumn=7, btnText="Cosh", bgColor="#3F4CFF", fgColor = "#cdd1d0", btnAction=lambda: myUtility.printOnMonitor("Cosh", monitor, isFunction=True))  # cosh
