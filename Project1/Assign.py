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

    def print(self, numIndents):
        if self.exprNonTerm != None:
            print(("\t" * numIndents) + self.identifier1 + "=", end = '') #indent by 1
            self.exprNonTerm.print(0)
            print(";")
        elif self.whichString == "new":
            print(("\t" * numIndents) + self.identifier1 + "=" + "new;")
        elif self.whichString == "ref":
            print(("\t" * numIndents) + self.identifier1 + "=" + "ref " + self.identifier2 + ";")

    def semantic(self, symbolTableGlobal, symbolTableLocal):
        if self.exprNonTerm != None:
            symbolTableLocal.append(self.identifier1)
            symbolTableLocal.append("=")
            self.exprNonTerm.semantic(symbolTableGlobal, symbolTableLocal)
            symbolTableLocal.append(";")
        elif self.whichString == "new":
            symbolTableLocal.append(self.identifier1)
            symbolTableLocal.append("=")
            symbolTableLocal.append("new")
            symbolTableLocal.append(";")
        elif self.whichString == "ref":
            symbolTableLocal.append(self.identifier1)
            symbolTableLocal.append("=")
            symbolTableLocal.append("ref")
            symbolTableLocal.append(self.identifier2)
            symbolTableLocal.append(";")