from Core import Core
from Expr import Expr


class Assign:
    def __init__(self):
        self.exprNonTerm = None
        self.whichString = ""
        self.identifier1 = ""
        self.identifier2 = ""

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.ID:
            print("ERROR: Token should be 'id'")
            quit()
        self.identifier1 = S.getID()
        S.nextToken()

        if S.currentToken() == Core.ASSIGN:
            S.nextToken()
            # if S.currentToken() != Core.NEW or S.currentToken() != Core.REF:
            #     self.exprNonTerm = Expr()
            #     self.exprNonTerm.parse(S)

        if S.currentToken() == Core.NEW:
            self.whichString = "new"
            S.nextToken()
        elif S.currentToken() == Core.REF:
            self.whichString = "ref"
            S.nextToken()
            self.identifier2 = S.getID()
            S.nextToken() ##extra to get the begin tok
        else:
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
        if self.exprNonTerm != None:
            print(numIndents + self.identifier1 + "=", end = '') #indent by 1
            self.exprNonTerm.print(0)
            print(";")
        elif self.whichString == "new":
            print(numIndents + self.identifier1 + "=" + "new;")
        elif self.whichString == "ref":
            print(numIndents + self.identifier1 + "=" + "ref " + self.identifier2 + ";")


