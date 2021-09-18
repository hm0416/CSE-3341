from Core import Core
from DeclSeq import DeclSeq
from StmtSeq import StmtSeq

class Prog:
    def __init__(self):
        self.ds = None
        self.ss = None

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.PROGRAM:
            print("ERROR: Token should be 'program'")
            quit()
        S.nextToken() #scanner starts at declSeq

        if S.currentToken() == Core.BEGIN:
            S.nextToken()
        else:
            self.ds = DeclSeq() # this class will handle the consuming of toks
            self.ds.parse(S) #consume all toks that make up declSeq
            S.nextToken() #begin tok
        self.ss = StmtSeq()
        self.ss.parse(S)

        # if S.currentToken() == Core.INT or S.currentToken() == Core.REF:
        #     self.ds = DeclSeq() # this class will handle the consuming of toks
        #     self.ds.parse(S) #consume all toks that make up declSeq
        #
        # if S.currentToken() != Core.BEGIN:
        #     print("ERROR: Token should be 'begin'")
        #     quit()
        # S.nextToken()
        # self.ss = StmtSeq()
        # self.ss.parse(S)

        if S.currentToken() != Core.END:
            print("ERROR: Token should be 'end'")
            quit()
        S.nextToken()
        if S.currentToken() != Core.EOF:
            print("ERROR: Program should be at the end of the file")
            quit()
        S.nextToken()

    def print(self):
        print("program")
        if self.ds != None:
            self.ds.print() #indent by 1
        print("begin")
        self.ss.print() #has to be there
        print("end")