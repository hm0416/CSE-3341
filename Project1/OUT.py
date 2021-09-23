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
            print("ERROR: Token should be ';'")
            quit()
        S.nextToken()

    def print(self, numIndents):
        print(("\t" * numIndents) + "output ", end = '')
        self.exprNonTerm.print(0)
        print(";")

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     symbolTableLocal.append("output")
    #     self.exprNonTerm.semantic(symbolTableGlobal, symbolTableLocal)
    #     symbolTableLocal.append(";")