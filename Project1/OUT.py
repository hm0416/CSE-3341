from Core import Core
from Expr import Expr


class OUT:
    # global exprNonTerm
    def __init__(self):
        self.exprNonTerm = None

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.OUTPUT:
            S.nextToken()
        self.exprNonTerm = Expr()
        self.exprNonTerm.parse(S)

        if S.currentToken() != Core.SEMICOLON:
            print("ERROR: Token should be ';'")
            quit()
        S.nextToken()

    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"

        return tab

    def print(self, numOfIndents):
        numIndents = "\t"
        print(numIndents + "output ", end = '')
        self.exprNonTerm.print(0)
        print(";")