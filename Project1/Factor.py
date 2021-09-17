from Core import Core


class Factor:
    def __init__(self):
        self.expr = None
        self.whichStr = 0 #0 for none, 1 for ID, 2 for CONST

    # no error checking needed here
    def parse(self, S):
        if S.currentToken() == Core.ID:
            self.whichStr = 1
            S.nextToken()
        elif S.currentToken() == Core.CONST:
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
            print("id")
        elif self.whichStr == 2:
            print("const")
        else:
            print("(")
            self.expr.print()
            print(")")
