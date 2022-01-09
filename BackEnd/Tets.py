
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





testCases = [
            "2 * 3 ",
            " 2 * 3 + 5",
            "40 / 4 / 5 / 2 * 2 + 1",
            "3.2 + 6.8",
            "( 2 * 3 )",
            #"ceil ( 2.3 )",
            #"cos ( sin ( 2 * 3 ) + 9 / 9 )",
    ]
print("======== RUNNING TEST CASES ========")
for expr in testCases:
    cal =  Cal.Calculator(expr, -1)
    result = cal.calculate()
    expr = ''.join([x for x in  list(expr) if x != " "])
    square_number = eval(expr)
    print(f"EXPRESSION: {expr} => {square_number == result}")
    























































