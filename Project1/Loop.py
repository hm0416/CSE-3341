from Core import Core
from Cond import Cond
from StmtSeq import StmtSeq

class Loop:
    def __init__(self):
        self.condNonTerm = None
        self.ss = None

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.WHILE:
            print("ERROR: Token should be 'while'")
            quit()
        S.nextToken()
        self.condNonTerm = Cond()
        self.condNonTerm.parse(S)

        if S.currentToken() == Core.BEGIN:
            S.nextToken()
        self.ss = StmtSeq()
        self.ss.parse(S)

        if S.currentToken() != Core.ENDWHILE:
            print("ERROR: Token should be 'endwhile'")
            quit()
        S.nextToken()

    def print(self, numIndents):
        print(("\t" * numIndents) + "while ", end = '')
        self.condNonTerm.print(0)
        print(" begin")
        self.ss.print(numIndents + 1) #has to be there
        print(("\t" * numIndents) + "endwhile")

    # def semantic(self):
