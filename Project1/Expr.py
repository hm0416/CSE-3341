import Core
import Term

class Expr:
    #potential children
    global term
    global expr
    operator = 0 #0 if no operation, 1 if addition, 2 if subtraction

    #no error checking needed here
    def parse(self, S):
        term = Term()
        term.parse(S)

        if S.currentToken() == Core.ADD:
            S.nextToken()
            operator = 1
            expr = Expr()
            expr.parse(S)
        elif S.currentToken() == Core.SUB:
            S.nextToken()
            operator = 2
            expr = Expr()
            expr.parse(S)

    def print(self):
        print("program")



