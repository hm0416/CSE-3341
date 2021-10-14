def initialize():
    global isRef
    global refID
    global varAfterRef
    global varAfterInt
    global needToPop
    global goInStmt
    global refDeclared
    global arrOfDeclared
    global isInt
    global addRef
    global addInt
    global isRefThen
    global onlyChar
    global ids
    global assignFrom
    global isRefArr
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
    varAfterInt = ""
    isRefArr = []
    addRef = False