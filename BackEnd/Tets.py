
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

# How to Pass it?
expr = "function sin 90"
expr = "31 / 1 + 2 * 2 / 5 - 9 / 4 * 2.5"

cal =  Cal.Calculator(expr, -1)
result = cal.calculate()






#expr = "142 / 6 / 7 / 2 + 1"

print(result)

square_number = eval("31 / 1 + 2 * 2 / 5 - 9 / 4 * 2.5")
print(square_number == result)























































