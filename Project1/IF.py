from Core import Core
from Cond import Cond
from StmtSeq import StmtSeq

class IF:
    def __init__(self):
        self.condNonTerm = None
        self.ss = None
        self.whichStr = 0 #0 for none, 1 for else

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.IF:
            print("ERROR: Token should be 'if'")
            quit()
        S.nextToken()
        self.condNonTerm = Cond()
        self.condNonTerm.parse(S)

        if S.currentToken() != Core.THEN:
            print("ERROR: Token should be 'then'")
            quit()
        S.nextToken()
        self.ss = StmtSeq()
        self.ss.parse(S)

        if S.currentToken() == Core.ELSE:
            self.whichStr == 1
            S.nextToken()
            self.ss = StmtSeq()
            self.ss.parse(S)
            if S.currentToken() != Core.ENDIF:
                print("ERROR: Token should be 'then'")
                quit()
            S.nextToken()
        elif S.currentToken() == Core.ENDIF:
            S.nextToken()

    def print(self):
        print("if ", end = '')
        self.condNonTerm.print()
        print(" then ")
        self.ss.print()
        if self.whichStr == 1:
            print("else ")
            self.ss.print()
            print("endif")
        else:
            print("endif")
