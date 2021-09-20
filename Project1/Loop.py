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

    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"

        return tab

    def print(self, numOfIndents):
        numIndents = "\t\t"
        print(numIndents + "while ", end = '')
        self.condNonTerm.print(0)
        print(" begin")
        self.ss.print(0) #has to be there
        print(numIndents + "endwhile")