from Core import Core
from Cmpr import Cmpr

class Cond:

    def __init__(self):
        self.condNonTerm = None
        self.cmprNonTerm = None
        self.whichStr = 0 #0 none, 1 for OR, 2 for negation

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.NEGATION:
            self.whichStr = 1
            S.nextToken()
            if S.currentToken() == Core.LPAREN:
                S.nextToken()
                self.condNonTerm = Cond()
                self.condNonTerm.parse(S)
                if S.currentToken() == Core.RPAREN:
                    S.nextToken()
                else:
                    print("ERROR: Right parenthesis expected")
                    quit()
            else:
                print("ERROR: Left parenthesis expected")
                quit()
        else:
            self.cmprNonTerm = Cmpr()
            self.cmprNonTerm.parse(S)
            if S.currentToken() == Core.OR:
                self.whichStr = 2
                S.nextToken()
                self.condNonTerm = Cond()
                self.condNonTerm.parse(S)

    def print(self, numOfIndents):
        if self.whichStr == 1:
            print("!(", end = '')
            self.condNonTerm.print(0)
            print(")", end = '')
        elif self.whichStr == 2:
            self.cmprNonTerm.print(0)
            print(" or ", end = '')
            self.condNonTerm.print(0)
        else:
            self.cmprNonTerm.print(0)

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     if self.whichStr == 1:
    #         symbolTableLocal.append("!(")
    #         self.condNonTerm.semantic(symbolTableGlobal, symbolTableLocal)
    #         symbolTableLocal.append(")")
    #     elif self.whichStr == 2:
    #         self.cmprNonTerm.semantic(symbolTableGlobal, symbolTableLocal)
    #         symbolTableLocal.append("or")
    #         self.condNonTerm.semantic(symbolTableGlobal, symbolTableLocal)
    #     else:
    #         self.cmprNonTerm.semantic(symbolTableGlobal, symbolTableLocal)

    def semantic(self, symTable, globalSymTable):
        if self.whichStr == 1:
            self.condNonTerm.semantic(symTable, globalSymTable)
        elif self.whichStr == 2:
            self.cmprNonTerm.semantic(symTable, globalSymTable)
            self.condNonTerm.semantic(symTable, globalSymTable)
        else:
            self.cmprNonTerm.semantic(symTable, globalSymTable)