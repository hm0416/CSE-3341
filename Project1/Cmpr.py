from Core import Core
from Expr import Expr

class Cmpr:
    def __init__(self):
        self.exprNonTerm1 = None
        self.exprNonTerm2 = None
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

    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"

        return tab

    def print(self, numOfIndents):
        numIndents = self.createIndents(numOfIndents)
        self.exprNonTerm1.print(0)
        if self.operator == 1:
            print("==", end = '')
            self.exprNonTerm2.print(0)
        elif self.operator == 2:
            print("<", end = '')
            self.exprNonTerm2.print(0)
        elif self.operator == 3:
            print("<=", end = '')
            self.exprNonTerm2.print(0)