
import Calculator as Cal



'''
Functions: 
    sin
    cos
    sinh
    cosh
    tan
    ctg
    ceil
    floor
    sqrt
    log
    exp
'''


expr = "32 / 3.2 + 2 * 2 / 5 - 9 / 4 * 2.5"
expr = "ceil ( 2.3 )"
cal =  Cal.Calculator(expr, -1)
result = cal.calculate()






#expr = "142 / 6 / 7 / 2 + 1"


print(f"My Output: {result}")
square_number = eval("32/3.2+2*2/5-9/4*2.5")
print(f"Eval Output: {square_number}")
print(square_number == result)























































