from Core import Core
from Cond import Cond
from StmtSeq import StmtSeq

class Loop:
    def __init__(self):
        self.condNonTerm = None
        self.ss = None

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.WHILE:
            print("ERROR")
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

    def print(self):
        print("while")
        self.condNonTerm.print()
        print("begin")
        self.ss.print() #has to be there
        print("endwhile")