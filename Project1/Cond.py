from Core import Core
from Cmpr import Cmpr

class Cond:

    def __init__(self):
        self.condNonTerm = None
        self.cmprNonTerm = None
        self.whichStr = 0 #0 none, 1 for OR, 2 for negation

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.NEGATION:
            self.whichStr = 1
            S.nextToken()
            if S.currentToken() == Core.LPAREN:
                S.nextToken()
                self.condNonTerm = Cond()
                self.condNonTerm.parse(S)
                if S.currentToken() == Core.RPAREN:
                    S.nextToken()
        else:
            self.cmprNonTerm = Cmpr()
            self.cmprNonTerm.parse(S)
            if S.currentToken() == Core.OR:
                self.whichStr = 2
                S.nextToken()
                self.condNonTerm = Cond()
                self.condNonTerm.parse(S)

    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"

        return tab

    def print(self, numOfIndents):
        numIndents = self.createIndents(numOfIndents)
        if self.whichStr == 1:
            print("!(", end = '')
            self.condNonTerm.print(0)
            print(")", end = '')
        elif self.whichStr == 2:
            self.cmprNonTerm.print(0)
            print(" or ", end = '')
            self.condNonTerm.print(0)
        else:
            self.cmprNonTerm.print(0)
