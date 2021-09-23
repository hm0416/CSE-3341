from Core import Core
from Expr import Expr

class Cmpr:
    def __init__(self):
        self.exprNonTerm1 = None #first expr
        self.exprNonTerm2 = None #second expr
        self.operator = 0 #0 for none, 1 for equal, 2 for less, 3 for lessequal

    def parse(self, S): #should not output anything unless error case
        self.exprNonTerm1 = Expr()
        self.exprNonTerm1.parse(S)
        if S.currentToken() == Core.EQUAL:
            self.operator = 1
            S.nextToken()
            self.exprNonTerm2 = Expr()
            self.exprNonTerm2.parse(S)
        elif S.currentToken() == Core.LESS:
            self.operator = 2
            S.nextToken()
            self.exprNonTerm2 = Expr()
            self.exprNonTerm2.parse(S)
        elif S.currentToken() == Core.LESSEQUAL:
            self.operator = 3
            S.nextToken()
            self.exprNonTerm2 = Expr()
            self.exprNonTerm2.parse(S)
        else:
            print("ERROR: Symbol not valid")
            quit()

    def print(self, numOfIndents):
        self.exprNonTerm1.print(1)
        if self.operator == 1:
            print("==", end = '')
            self.exprNonTerm2.print(0)
        elif self.operator == 2:
            print("<", end = '')
            self.exprNonTerm2.print(0)
        elif self.operator == 3:
            print("<=", end = '')
            self.exprNonTerm2.print(0)

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     self.exprNonTerm1.semantic(symbolTableGlobal, symbolTableLocal)
    #     if self.operator == 1:
    #         symbolTableLocal.append("==")
    #         self.exprNonTerm2.semantic(symbolTableGlobal, symbolTableLocal)
    #     elif self.operator == 2:
    #         symbolTableLocal.append("<")
    #         self.exprNonTerm2.semantic(symbolTableGlobal, symbolTableLocal)
    #     elif self.operator == 3:
    #         symbolTableLocal.append("<=")
    #         self.exprNonTerm2.semantic(symbolTableGlobal, symbolTableLocal)

    def semantic(self, symTable, globalSymTable):
        self.exprNonTerm1.semantic(symTable, globalSymTable)
        if self.operator == 1:
            self.exprNonTerm2.semantic(symTable, globalSymTable)
        elif self.operator == 2:
            self.exprNonTerm2.semantic(symTable, globalSymTable)
        elif self.operator == 3:
            self.exprNonTerm2.semantic(symTable, globalSymTable)