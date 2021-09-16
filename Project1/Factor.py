from Core import Core


class Factor:
    # potential children
    # global exprNonTerm

    # no error checking needed here
    def parse(self, S):
        if S.currentToken() == Core.ID:
            S.nextToken()
        elif S.currentToken() == Core.CONST:
            S.nextToken()
        elif S.currentToken() == Core.LPAREN:
            S.nextToken()
            from Expr import Expr
            expr = Expr()
            expr.parse(S)
            if S.currentToken() == Core.RPAREN:
                S.nextToken()

    # def print(self):
    #     print("program")

