from Core import Core


class Factor:
    def __init__(self):
        self.expr = None
        self.identifier = ""
        self.const = 0
        self.whichStr = 0 #0 for none, 1 for ID, 2 for CONST

    # no error checking needed here
    def parse(self, S):
        if S.currentToken() == Core.ID:
            self.identifier = S.getID()
            self.whichStr = 1
            S.nextToken()
        elif S.currentToken() == Core.CONST:
            self.const = S.getCONST()
            self.whichStr = 2
            S.nextToken()
        elif S.currentToken() == Core.LPAREN:
            S.nextToken()
            from Expr import Expr
            self.expr = Expr()
            self.expr.parse(S)
            if S.currentToken() == Core.RPAREN:
                S.nextToken()

    def print(self):
        if self.whichStr == 1:
            print(self.identifier, end = '')
        elif self.whichStr == 2:
            print(self.const, end = '')
        else:
            print(" (", end = '')
            self.expr.print()
            print(")", end = '')
