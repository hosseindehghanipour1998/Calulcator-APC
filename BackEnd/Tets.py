
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
#expr = "1 + 2 * 3 * cos ( sin ( 89 + 1 ) ) * tan ( 0 ) - 1"
expr = "2 ^ 2 ^ 3"
 
#expr = "31 / 1 + 2 * 2 / 5 - 9 / 4 * 2.5"

cal =  Cal.Calculator(expr, -1)
result = cal.calculate()






#expr = "142 / 6 / 7 / 2 + 1"

print(result)
import re
p = r"^"
re.sub(p,"**",expr)
square_number = eval(expr)
print(square_number == result)























































