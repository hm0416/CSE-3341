from Core import Core
from Expr import Expr


class OUT:
    def __init__(self):
        self.exprNonTerm = None

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.OUTPUT:
            S.nextToken()
        else:
            print("ERROR: Token should be 'output'")
            quit()
        self.exprNonTerm = Expr()
        self.exprNonTerm.parse(S)

        if S.currentToken() != Core.SEMICOLON:
            print("ERROR: Token should be ';', token should NOT be a " + S.currentToken().name)
            quit()
        S.nextToken()

    def print(self, numIndents):
        print(("\t" * numIndents) + "output ", end = '')
        self.exprNonTerm.print()
        print(";")
