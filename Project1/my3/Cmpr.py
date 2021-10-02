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
            if S.currentToken() == Core.ASSIGN:
                print("ERROR: ASSIGN is in the condition.")
                quit()
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

    def print(self):
        self.exprNonTerm1.print()
        if self.operator == 1:
            print("==", end = '')
            self.exprNonTerm2.print()
        elif self.operator == 2:
            print("<", end = '')
            self.exprNonTerm2.print()
        elif self.operator == 3:
            print("<=", end = '')
            self.exprNonTerm2.print()

    def execute(self):
        value = self.exprNonTerm1.execute()
        if self.operator == 1:
            if value == self.exprNonTerm2.execute():
                value = True
            else:
                value = False
        elif self.operator == 2:
            if value < self.exprNonTerm2.execute():
                value = True
            else:
                value = False
        elif self.operator == 3:
            if value <= self.exprNonTerm2.execute():
                value = True
            else:
                value = False

        return value