def initialize():
    global isRef
    global refID
    global varAfterRef
    global needToPop
    global goInStmt
    global refDeclared
    global arrOfDeclared
    global isInt
    global addInt
    global isRefThen
    global onlyChar
    global ids
    global assignFrom
    isRef = False
    refID = ""
    varAfterRef = ""
    needToPop = False
    goInStmt = False
    refDeclared = False
    arrOfDeclared = {}
    isInt = []
    isRefThen = False
    addInt = False
    onlyChar = False
    ids = [{}]
    assignFrom = ""