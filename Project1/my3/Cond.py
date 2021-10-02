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
                    print("ERROR: Right parenthesis expected")
                    quit()
            else:
                print("ERROR: Left parenthesis expected, token should NOT be a " + S.currentToken().name)
                quit()
        else:
            self.cmprNonTerm = Cmpr()
            self.cmprNonTerm.parse(S)
            if S.currentToken() == Core.OR:
                self.whichStr = 2
                S.nextToken()
                self.condNonTerm = Cond()
                self.condNonTerm.parse(S)

    def print(self):
        if self.whichStr == 1:
            print("!(", end = '')
            self.condNonTerm.print()
            print(")", end = '')
        elif self.whichStr == 2:
            self.cmprNonTerm.print()
            print(" or ", end = '')
            self.condNonTerm.print()
        else:
            self.cmprNonTerm.print()

    def execute(self):
        value = False
        if self.whichStr == 1:
            value = not (self.condNonTerm.execute())
        elif self.whichStr == 2:
            value = self.cmprNonTerm.execute() or self.condNonTerm.execute()
        else:
            value = self.cmprNonTerm.execute()

        return value
