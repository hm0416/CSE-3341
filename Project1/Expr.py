from Core import Core
from Term import Term


class Expr:
    def __init__(self):
        self.term = None
        self.exprNonTerm = None
        self.operator = 0  # 0 if no operation, 1 if addition, 2 if subtraction

    # no error checking needed here
    def parse(self, S):
        self.term = Term()
        self.term.parse(S)

        if S.currentToken() == Core.ADD:
            S.nextToken()
            self.operator = 1
            self.exprNonTerm = Expr()
            self.exprNonTerm.parse(S)
        elif S.currentToken() == Core.SUB:
            S.nextToken()
            self.operator = 2
            self.exprNonTerm = Expr()
            self.exprNonTerm.parse(S)

    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"

        return tab

    def print(self, numOfIndents):
        numIndents = self.createIndents(numOfIndents)
        self.term.print(0)
        if self.exprNonTerm != None:
            if self.operator == 1:
                print("+", end = '')
                self.exprNonTerm.print(0)
            elif self.operator == 2:
                print("-", end = '')
                self.exprNonTerm.print(0)
