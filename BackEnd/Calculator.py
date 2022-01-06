import re
import math

class Calculator :

    def __init__(self, expression , inputX):
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
        self.expr = list(expression.split())
        self.operatorsList = {'+' , '-' , '/' , '*' , '^'}
        self.operatorPrecedences = { "+" : 1 , "-": 1 , "/" : 3 , "*" : 3 , "^" : 4 }
        self.x = inputX
        self.isCallingFunction = (True if ( str(self.expr[0]).upper() == "FUNCTION") else False)
        
        ###### Used for debugging (Start)######
        print(f"Expression : {self.expr} \n Len : {len(self.expr)} \n input : { self.x} \n Function? {self.isCallingFunction}\n ")
        ###### Used for debugging (End)######

    def operandAction(self,operator, input1 , input2):
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
        if(operator == "+"):
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
        operand = math.radians(operand)
        switchCase = {
            "tan": "math.tan(operand)",
            "ctg": "1/math.tan(operand)",
            "sin": "math.sin(operand)",
            "cos": "math.cos(operand)",
            "ceil": "math.ceil(operand)",
            "floor": "math.floor(operand)",
            "sqrt": "math.sqrt(operand)",
            "log": "math.log(operand)",
            "exp": "math.exp(operand)",
            "cosh": "math.cosh(operand)",
            "sinh": "math.sinh(operand)"
            }
        result =  eval(switchCase.get(functionName, "Function Not Found"))
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
            #print(f"Read Character: {character}")
            ###### Used for debugging (End) ######
            
            # If character == Operator
            if ( character in self.operatorsList):
                # There was sth in operator stack from before
                if ( len(self.operatorStack) > 0 ):
                    
                    # Power and Open Paranthesis should be considered seperately because they affect the precedence of the operation.
                    if ( ( character == "^" and self.operatorStack[-1] == "^") or(self.operatorStack[-1] == '(') or (self.operatorPrecedences[character] > self.operatorPrecedences[self.operatorStack[-1]]) ):
                        self.operatorStack.append(character)
                    
                    # If the precedence of the current operator is higher than the precedence of the next operator, we should calculate the previous one before pushing the new operator
                    elif ((self.operatorPrecedences[character] <= self.operatorPrecedences[self.operatorStack[-1]]) ):

                        if(len(self.operandStack) > 0):
                            # Calculate the previous operator inside the stack
                            a = self.operandStack.pop()
                            b = self.operandStack.pop()
                            result = self.operandAction(self.operatorStack.pop(), b , a)
                            self.operandStack.append(result)
                            
                            # Also push the current operator inside the stack
                            self.operatorStack.append(character)
                    else:
                        self.operatorStack.append(character)
                else :
                    self.operatorStack.append(character)
            
            elif ( character == '('):
                self.operatorStack.append(character)
            
            elif(character == ')'):
                stackTop = self.operatorStack.pop()
                while ( stackTop != '('):
                    a = self.operandStack.pop()
                    b = self.operandStack.pop()
                    result = self.operandAction(stackTop, b, a)
                    self.operandStack.append(result)
                    stackTop = self.operatorStack.pop()
            
            # If Character == Varibale X 
            elif ( character.isalpha() == True ):
                self.operandStack.append(self.x)
                
                
            # If Character == Operand (Number)
            elif ( (character.isdigit() == True) or (self.is_float(character)) ):
                self.operandStack.append(float(character))
       
        # End of Loop
        while (len(self.operatorStack) > 0):
            try:
                operator = self.operatorStack.pop()
                a = self.operandStack.pop()
                b = self.operandStack.pop()
                result = self.operandAction(operator, b, a)
                self.operandStack.append(result)
            except:
                 raise Exception("Operators Are More Than Operands. Fix it :D (1)")
                 
            ###### Used for debugging (Start)######
            #print("Operation: " + str(operator) + " Operands: " + str(a) + " " + str(b))
            ###### Used for debugging (End)######
        
        return self.operandStack.pop()


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
            if(self.isCallingFunction):          
                functionName =  str(self.expr[1]).lower()         
                operand =  float(self.expr[2])
                result = self.calculateFunction(functionName, operand)
                
                ###### Used for debugging (Start)######
                print(f"Expr: {self.expr}")
                print(f"Function Name: ({str(self.expr[1]).lower()})")
                print(f"Function Name: {functionName} | Operand: {operand}")
                print(f"Results: {result}")
                ###### Used for debugging (End)######
                
            else:
                result = self.calculateOperator()
        except:
            raise Exception("Backend Cannot Support the Entered Exporession. Fix it :D (2)")
            
        return result
            
            
        