import re
import math


class Calculator:

    def __init__(self, expression, inputX):
        '''

        Parameters
        ----------
        expression : String
            TRhe Entered Expression from the front.
        inputX : Integer
            The amount that will be replaced by the variable x.
        Returns
        -------
        None. An instance object of Calculator Class.
        '''

        self.length = len(expression)
        self.operatorStack = []
        self.operandStack = []
        self.expr = list((expression).lower().split())
        self.operatorsList = {'+', '-', '/', '*', '^'}
        self.operatorPrecedences = {
            "+": 1,
            "-": 1,
            "/": 3,
            "*": 3,
            "^": 4,
            "sin": 5,
            "cos": 5,
            "tan": 5,
            "ctg": 5,
            "ceil": 5,
            "floor": 5,
            "sqrt": 5,
            "log": 5,
            "exp": 5,
            "cosh": 5,
            "sinh": 5
        }
        self.functionsList = {"sin", "cos", "tan", "ctg", "ceil", "floor", "sqrt", "log", "exp", "cosh", "sinh"}
        self.x = inputX

        ###### Used for debugging (Start)######
        print(f"Expression : {self.expr} \n Len : {len(self.expr)} \n input : {self.x} \n ")
        ###### Used for debugging (End)######

    def operandAction(self, operator, input1, input2):
        '''
        Parameters
        ----------
        operator : Chatracter (String)
            The Operator of the action. Can be + * / - ^
        input1 : Integer
            The first operand that the operator is applied on.
        input2 : Integer
            The second operand needed to complete both sides of an operator.
        Returns
        -------
        Integer
            The calculated value of the operation with the given operands .
        '''
        if (operator == "+"):
            return (input1 + input2)
        elif (operator == '-'):
            return (input1 - input2)
        elif (operator == '/'):
            return (input1 / input2)
        elif (operator == '*'):
            return (input1 * input2)
        elif (operator == '^'):
            return (input1 ** input2)

    def is_float(self, string):
        '''
        Parameters
        ----------
        string : String
            The String form of the number we want to check if is float or not.
        Returns
        -------
        TYPE: Boolean
            Checks if the passed number in String format is a float number or not.


        Reference of This Code:
        https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python#comment101879949_38329481

        '''

        _float_regexp = re.compile(r"^[-+]?(?:\b[0-9]+(?:\.[0-9]*)?|\.[0-9]+\b)(?:[eE][-+]?[0-9]+\b)?$").match
        return True if _float_regexp(string) else False

    def calculateFunction(self, functionName, operand):
        '''
        This function is called whenever we have passed a function that requires the help math.py library in Python.
        Parameters
        ----------
        functionName : String
            Name of the passed Function. Can be sin, cos, tan, ctg, ceil, floor, sinh, cosh, exp, sqrt, exp
        operand : Integer
            The Operand that the function should be apllied on.
        Returns
        -------
        result : Integer, String
            If the function name is entered correctly it will return an integer which is the calculated output.
            Otherwise, if the name of the function is not in our function list or entered incorrecly, it returns a "Function Not Found" String as output.
        '''
        operandInRadian = math.radians(operand)
        switchCase = {
            "tan": "math.tan(operandInRadian)",
            "ctg": "1/math.tan(operandInRadian)",
            "sin": "math.sin(operandInRadian)",
            "cos": "math.cos(operandInRadian)",
            "ceil": "math.ceil(operand)",
            "floor": "math.floor(operand)",
            "sqrt": "math.sqrt(operand)",
            "log": "math.log(operand)",
            "exp": "math.exp(operand)",
            "cosh": "math.cosh(operandInRadian)",
            "sinh": "math.sinh(operandInRadian)"}
        result = eval(switchCase.get(functionName, "Function Not Found"))
        print(f"{functionName}({operandInRadian} R) = {result}")
        print(f"{functionName}({operand}) = {result}")
        return result

    def calculateOperator(self):
        '''
        Parameters: Gets nothing because it uses the expression variable from the class.
        Returns
        -------
        TYPE: Integer
            returns the value of the calculated expression. The expression may include sophisticated precedences and this function overcomes the problem.
        '''
        for character in self.expr:
            ###### Used for debugging (Start)######
            print(f"Read Character: {character}")
            # print(f"operator Stack: {self.operatorStack}")
            # print(f"Operand Stack: {self.operandStack}")
            ###### Used for debugging (End) ######

            # If character == Operator
            if (character in self.operatorsList or character in self.functionsList):
                # There was sth in operator stack from before
                if (len(self.operatorStack) > 0):

                    # Power and Open Paranthesis should be considered seperately because they affect the precedence of the operation.
                    if ((character == "^" and self.operatorStack[-1] == "^") or (self.operatorStack[-1] == '(') or (
                            self.operatorPrecedences[character] > self.operatorPrecedences[self.operatorStack[-1]])):
                        self.operatorStack.append(character)


                    # If the precedence of the current operator is higher than the precedence of the next operator, we should calculate the previous one before pushing the new operator
                    elif ((self.operatorPrecedences[character] <= self.operatorPrecedences[self.operatorStack[-1]])):

                        if (len(self.operandStack) > 0):
                            operator = self.operatorStack.pop()
                            if (operator in self.functionsList):
                                self.handleFunctionCharacter(operator)

                            else:
                                # Calculate the previous operator inside the stack
                                self.handleOperatorCharacter(operator)

                            # Also push the current operator inside the stack
                            self.operatorStack.append(character)
                    else:
                        self.operatorStack.append(character)

                else:
                    self.operatorStack.append(character)


            elif (character == '('):
                self.operatorStack.append(character)

            elif (character == ')'):
                stackTop = self.operatorStack.pop()
                while (stackTop != '('):

                    if (stackTop in self.functionsList):
                        self.handleFunctionCharacter(stackTop)
                        stackTop = self.operatorStack.pop()

                    else:
                        self.handleOperatorCharacter(stackTop)
                        stackTop = self.operatorStack.pop()

                print(self.operatorStack)

                stackTop = self.operatorStack[-1]
                if (stackTop in self.functionsList):
                    stackTop = self.operatorStack.pop()
                    self.handleFunctionCharacter(stackTop)

            # If Character == Varibale X
            elif (character.isalpha() == True):
                self.operandStack.append(self.x)


            # If Character == Operand (Number)
            elif ((character.isdigit() == True) or (self.is_float(character))):
                self.operandStack.append(float(character))

        # End of Loop
        while (len(self.operatorStack) > 0):
            try:
                operator = self.operatorStack.pop()
                if (operator in self.functionsList):
                    self.handleFunctionCharacter(operator)

                else:
                    self.handleOperatorCharacter(operator)

            except:
                raise Exception("Operators Are More Than Operands. Fix it :D (1)")

            ###### Used for debugging (Start)######
            # print("Operation: " + str(operator) + " Operands: " + str(a) + " " + str(b))
            ###### Used for debugging (End)######

        return self.operandStack.pop()

    def handleFunctionCharacter(self, operator):
        functionName = operator.lower()
        argument = self.operandStack.pop()
        result = self.calculateFunction(functionName, argument)
        self.operandStack.append(result)

    def handleOperatorCharacter(self, operator):

        a = self.operandStack.pop()
        b = self.operandStack.pop()
        result = self.operandAction(operator, b, a)
        self.operandStack.append(result)

    def calculate(self):

        '''
        Returns
        -------
        result : Integer, String
            If the name of the entered function is incorrect, it returns a "Function Not Found" String as expalined in the description
            of function "self.calculateFunction()". Otherwise, it calculates the output amount and returns the output result.
        '''
        result = None
        try:
            result = self.calculateOperator()
        except:
            raise Exception("Backend Cannot Support the Entered Exporession. Fix it :D (2)")
            # return None

        return result
