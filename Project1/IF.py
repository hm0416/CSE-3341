from Core import Core
from Cond import Cond
from StmtSeq import StmtSeq

class IF:
    def __init__(self):
        self.condNonTerm = None
        self.ss = None
        self.elseSS = None #second stmtSeq when there is an else statment

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.IF:
            print("ERROR: Token should be 'if'")
            quit()
        S.nextToken()
        self.condNonTerm = Cond()
        self.condNonTerm.parse(S)

        if S.currentToken() != Core.THEN:
            print("ERROR: Token should be 'then', token should NOT be a " + S.currentToken().name)
            quit()
        S.nextToken()
        self.ss = StmtSeq()
        self.ss.parse(S)

        if S.currentToken() == Core.ELSE:
            S.nextToken()
            self.elseSS = StmtSeq()
            self.elseSS.parse(S)
        if S.currentToken() != Core.ENDIF:
            print("ERROR: Token should be 'endif', token should NOT be a " + S.currentToken().name)
            quit()
        S.nextToken()

    def print(self, numIndents):
        print(("\t" * numIndents) + "if ", end = '')
        self.condNonTerm.print()
        print(" then")
        self.ss.print(numIndents + 1)
        if self.elseSS != None:
            print(("\t" * numIndents) + "else")
            self.elseSS.print(numIndents + 1)
            print(("\t" * numIndents) + "endif")
        else:
            print(("\t" * numIndents) + "endif")
