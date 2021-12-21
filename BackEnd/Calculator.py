import re

class Calculator :

    def __init__(self, expression , inputX):
        self.length = len(expression)
        self.operatorStack = []
        self.operandStack = []
        self.expr = expression.split()
        self.operatorsList = {'+' , '-' , '/' , '*' , '^'}
        self.operatorPrecedences = { "+" : 1 , "-": 1 , "/" : 3 , "*" : 3 , "^" : 4 }
        self.x = inputX
        print("Expression : {%s} \n Len : {%d} \n input : {%d} \n " %(self.expr , len(self.expr) , self.x))

    def operandAction(self,operand, input1 , input2):

        if(operand == "+"):
            return (input1 + input2)
        elif (operand == '-'):
            return (input1 - input2)
        elif (operand == '/'):
            return (input1 / input2)
        elif (operand == '*'):
            return (input1 * input2)
        elif (operand == '^'):
            return (input1 ** input2)


    def is_float(self,string):
        #Reference: https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python#comment101879949_38329481
        _float_regexp = re.compile(r"^[-+]?(?:\b[0-9]+(?:\.[0-9]*)?|\.[0-9]+\b)(?:[eE][-+]?[0-9]+\b)?$").match
        return True if _float_regexp(string) else False
    
    def calculate(self):
        for character in self.expr:
            print(f"Read Character: {character}")
            
            # If character == Operator
            if ( character in self.operatorsList):
                # There was sth in operator stack from before
                if ( len(self.operatorStack) > 0 ):

                    if ( ( character == "^" and self.operatorStack[-1] == "^") or(self.operatorStack[-1] == '(') or (self.operatorPrecedences[character] > self.operatorPrecedences[self.operatorStack[-1]]) ):
                        self.operatorStack.append(character)

                    elif ((self.operatorPrecedences[character] <= self.operatorPrecedences[self.operatorStack[-1]]) ):

                        if(len(self.operandStack) > 0):
                            a = self.operandStack.pop()
                            b = self.operandStack.pop()
                            result = self.operandAction(self.operatorStack.pop(), b , a)
                            self.operandStack.append(result)
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
            
            # If Character == Variable
            elif ( character.isalpha() == True ):
                self.operandStack.append(self.x)
                
                
            # If Character == Number
            elif ( (character.isdigit() == True) or (self.is_float(character)) ):
                self.operandStack.append(float(character))
        # End of Loop
        while (len(self.operatorStack) > 0): # FIX: Uncomment This
        #if(len(self.operatorStack) > 0):
            operator = self.operatorStack.pop()
            a = self.operandStack.pop()
            b = self.operandStack.pop()
            result = self.operandAction(operator, b, a)
            self.operandStack.append(result)
            print("Operation: " + str(operator) + " Operands: " + str(a) + " " + str(b))

        return self.operandStack.pop()
