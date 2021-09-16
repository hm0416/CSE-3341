from Core import Core
from Term import Term

class Expr:
    def __int__(self):
        self.term = None
        self.expr = None
        self.operator = 0 # 0 if no operation, 1 if addition, 2 if subtraction
    # no error checking needed here
    def parse(self, S):
        self.term = Term()
        self.term.parse(S)

        if S.currentToken() == Core.ADD:
            S.nextToken()
            self.operator = 1
            self.expr = Expr()
            self.expr.parse(S)
        elif S.currentToken() == Core.SUB:
            S.nextToken()
            self.operator = 2
            self.expr = Expr()
            self.expr.parse(S)

    def print(self):
        self.term.print()
        if self.operator == 1:
            print("+")
            self.expr.print()
        elif self.operator == 2:
            print("-")
            self.expr.print()


