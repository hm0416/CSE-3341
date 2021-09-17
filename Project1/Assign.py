from Core import Core
from Expr import Expr


class Assign:
    def __init__(self):
        self.exprNonTerm = None
        self.whichString = ""
        self.identifier = ""

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.ID:
            print("ERROR: Token should be 'id'")
            quit()
        self.identifier = S.getID()
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
        if self.exprNonTerm != None:
            print(self.identifier + " = ", end = '') #indent by 1
            self.exprNonTerm.print()
            print(";")
        elif self.whichString == "new":
            print(self.identifier + " = " + " new ;")
        elif self.whichString == "ref":
            print(self.identifier + " = " + " ref " + self.identifier + " ;")


