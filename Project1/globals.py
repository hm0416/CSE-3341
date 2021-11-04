def initialize():
    global formals #list of formal parameters
    global bod #the body of the function
    global isFunc #determines if a function has been declared
    global funcDeclName #name of the declared function so can use with error message
    global listOfFuncParams
    isFunc = False
    formals = None
    bod = None
    funcDeclName = ""
    listOfFuncParams = []
