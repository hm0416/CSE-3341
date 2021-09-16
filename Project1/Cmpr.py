from Core import Core
from Expr import Expr

class Cmpr:
    def __init__(self):
        self.exprNonTerm = None
        self.operator = 0 #0 for none, 1 for equal, 2 for less, 3 for lessequal

    def parse(self, S): #should not output anything unless error case
        self.exprNonTerm = Expr()
        self.exprNonTerm.parse(S)
        if S.currentToken() == Core.EQUAL:
            self.operator = 1
            S.nextToken()
            self.exprNonTerm = Expr()
            self.exprNonTerm.parse(S)
        elif S.currentToken() == Core.LESS:
            self.operator = 2
            S.nextToken()
            self.exprNonTerm = Expr()
            self.exprNonTerm.parse(S)
        elif S.currentToken() == Core.LESSEQUAL:
            self.operator = 3
            S.nextToken()
            self.exprNonTerm = Expr()
            self.exprNonTerm.parse(S)

    def print(self):
        self.exprNonTerm.print()
        if self.operator == 1:
            print("=")
            self.exprNonTerm.print()
        elif self.operator == 2:
            print("<")
            self.exprNonTerm.print()
        elif self.operator == 3:
            print("<=")
            self.exprNonTerm.print()