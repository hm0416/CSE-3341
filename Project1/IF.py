from Core import Core
from Cond import Cond
from StmtSeq import StmtSeq

class IF:
    def __init__(self):
        self.condNonTerm = None
        self.ss = None
        self.elseSS = None
        # self.whichStr = 0 #0 for none, 1 for else

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
            # self.whichStr = 1
            S.nextToken()
            self.elseSS = StmtSeq()
            self.elseSS.parse(S)
        if S.currentToken() != Core.ENDIF:
            print("ERROR: Token should be 'then'")
            quit()
        S.nextToken()

    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"

        return tab

    def print(self, numOfIndents):
        numIndents = "\t"
        print(numIndents + "if ", end = '')
        self.condNonTerm.print(0)
        print(" then")
        print("\t", end = '')
        self.ss.print(0)
        if self.elseSS != None:
            # if self.whichStr == 1:
            print(numIndents + "else ")
            print("\t", end = '')
            self.elseSS.print(0)
            print(numIndents + "endif")
        else:
            print(numIndents + "endif")
