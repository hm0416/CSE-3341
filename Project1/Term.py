from Core import Core
from Factor import Factor

class Term:
    def __init__(self):
        self.factorNonTerm = None
        self.termNonTerm = None
        self.operator = 0 #0 none, 1 is mult

    #no error checking needed here
    def parse(self, S):
        self.factorNonTerm = Factor()
        self.factorNonTerm.parse(S)

        if S.currentToken() == Core.MULT:
            self.operator = 1
            S.nextToken()
            self.termNonTerm = Term()
            self.termNonTerm.parse(S)

    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"

        return tab

    def print(self, numOfIndents):
        numIndents = self.createIndents(numOfIndents)
        self.factorNonTerm.print(0)
        if self.operator == 1:
            print("*", end = '')
            self.termNonTerm.print(0)




