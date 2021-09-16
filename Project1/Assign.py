from Core import Core
from Expr import Expr


class Assign:
    def __init__(self):
        self.exprNonTerm = None
        self.whichString = ""

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.ID:
            print("ERROR")
            quit()
        S.nextToken()

        if S.currentToken() == Core.ASSIGN:
            S.nextToken()
            if S.currentToken() != Core.NEW or S.currentToken() != Core.REF:
                self.exprNonTerm = Expr()
                self.exprNonTerm.parse(S)

        if S.currentToken() == Core.NEW:
            self.whichString = "new"
            S.nextToken()
        if S.currentToken() == Core.REF:
            self.whichString = "ref"
            S.nextToken()

        if S.currentToken() != Core.SEMICOLON:
            print("ERROR: Token should be ';'")
            quit()
        S.nextToken()

    def print(self):
        print("id")
        print("=")
        if self.exprNonTerm != None:
            self.exprNonTerm.print() #indent by 1
        elif self.whichString == "new":
            print("new")
        elif self.whichString == "ref":
            print("ref")
            print("id")
        print(";")

