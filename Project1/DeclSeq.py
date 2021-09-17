from Core import Core
from Decl import Decl

class DeclSeq:
    def __init__(self):
        self.d = None
        self.ds = None

    def parse(self, S): #should not output anything unless error case
        self.d = Decl()
        self.d.parse(S)

        # if S.currentToken() == Core.BEGIN:
        #     S.nextToken()
        if S.currentToken() == Core.INT or S.currentToken() == Core.REF:
            self.ds = DeclSeq() # this class will handle the consuming of toks
            self.ds.parse(S) #consume all toks that make up declSeq

    def print(self):
        self.d.print()
        if self.ds != None:
            self.ds.print()