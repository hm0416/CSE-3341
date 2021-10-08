def initialize():
    global isRef
    global refID
    global varAfterRef
    global needToPop
    global goInStmt
    global refDeclared;
    isRef = False
    refID = ""
    varAfterRef = ""
    needToPop = False
    goInStmt = False
    refDeclared = False