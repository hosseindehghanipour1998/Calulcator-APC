
import Calculator as Cal



expr = "2 ^ 1 ^ 3"
#expr = "142 / 6 / 7 / 2 + 1"
cal =  Cal.Calculator(expr, -1)
result = cal.calculate()
print(result)

square_number = eval('2**1**3')
print(square_number)

