def initialize():
    global isRef #if LHS is equal to a ref of another variable
    global refID #gets ID of the declared reference
    global needToPop #determines when to remove a dictionary from the parser.ids list
    global goInStmt #determines if in a new scope
    global arrOfDeclaredWithNew #array of variables that have been declared with "new" keyword - helps with ref error message
    global arrOfDeclared #array of decalred int variables - helps when there are multiple declared variables separated by a comma
    global addDeclaredVar #the additional variable declaration
    isRef = False
    refID = ""
    needToPop = False
    goInStmt = False
    arrOfDeclaredWithNew = {}
    arrOfDeclared = []
    addDeclaredVar = False