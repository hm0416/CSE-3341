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
            print("ERROR: Token should be 'then'")
            quit()
        S.nextToken()
        self.ss = StmtSeq()
        self.ss.parse(S)

        if S.currentToken() == Core.ELSE:
            S.nextToken()
            self.elseSS = StmtSeq()
            self.elseSS.parse(S)
        if S.currentToken() != Core.ENDIF:
            print("ERROR: Token should be 'endif'")
            quit()
        S.nextToken()

    def print(self, numIndents):
        print(("\t" * numIndents) + "if ", end = '')
        self.condNonTerm.print(0)
        print(" then")
        self.ss.print(numIndents + 1)
        if self.elseSS != None:
            print(("\t" * numIndents) + "else")
            self.elseSS.print(numIndents + 1)
            print(("\t" * numIndents) + "endif")
        else:
            print(("\t" * numIndents) + "endif")

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     symbolTableLocal.append("if")
    #     self.condNonTerm.semantic(symbolTableGlobal, symbolTableLocal)
    #     symbolTableLocal.append("then")
    #     self.ss.semantic(symbolTableGlobal, symbolTableLocal)
    #     if self.elseSS != None:
    #         symbolTableLocal.append("else")
    #         self.elseSS.semantic(symbolTableGlobal, symbolTableLocal)
    #         symbolTableLocal.append("endif")
    #     else:
    #         symbolTableLocal.append("endif")

    def semantic(self, symTable, globalSymTable, indx):
        symTable.append({}) #new scope
        self.condNonTerm.semantic(symTable, globalSymTable)
        self.ss.semantic(symTable, globalSymTable, len(symTable)-1)
        if self.elseSS != None:
            self.elseSS.semantic(symTable, globalSymTable, len(symTable)-1)
