
import Calculator as Cal



expr = "3 / 1 + 2 * 2 / 5 - 9 / 4 * 2.5"
#expr = "142 / 6 / 7 / 2 + 1"
cal =  Cal.Calculator(expr, -1)
result = cal.calculate()
print(result)

square_number = eval("3 / 1 + 2 * 2 / 5 - 9 / 4 * 2.5")
print(square_number == result)

