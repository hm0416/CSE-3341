from Core import Core
from Decl import Decl

class DeclSeq:
    def __init__(self):
        self.d = None
        self.ds = None

    def parse(self, S): #should not output anything unless error case
        self.d = Decl()
        self.d.parse(S)

        if S.currentToken() != Core.BEGIN:
            self.ds = DeclSeq() # this class will handle the consuming of toks
            self.ds.parse(S) #consume all toks that make up declSeq
        else:
            S.nextToken()

        # if S.currentToken() == Core.BEGIN:
        #     S.nextToken()
        # if S.currentToken() == Core.INT or S.currentToken() == Core.REF:
        #     self.ds = DeclSeq() # this class will handle the consuming of toks
        #     self.ds.parse(S) #consume all toks that make up declSeq

    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"

        return tab

    def print(self, numOfIndents):
        numIndents = self.createIndents(numOfIndents)
        self.d.print(0)
        if self.ds != None:
            self.ds.print(0)