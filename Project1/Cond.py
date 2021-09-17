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
                condNonTerm = Cond()
                condNonTerm.parse(S)
                if S.currentToken() == Core.RPAREN:
                    S.nextToken()
        else:
            cmprNonTerm = Cmpr()
            cmprNonTerm.parse(S)
            if S.currentToken() == Core.OR:
                self.whichStr = 2
                S.nextToken()
                condNonTerm = Cond()
                condNonTerm.parse(S)

    def print(self):
        if self.whichStr == 1:
            print("!")
            print("(")
            self.condNonTerm.print()
            print(")")
        elif self.whichStr == 2:
            self.cmprNonTerm.print()
            print("or")
            self.condNonTerm.print()
        else:
            self.cmprNonTerm.print()
