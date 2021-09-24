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

    def print(self, numOfIndents):
        self.factorNonTerm.print(1)
        if self.operator == 1:
            print("*", end = '')
            self.termNonTerm.print(0)
