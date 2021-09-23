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

    def print(self, numOfIndents):
        self.d.print(numOfIndents)
        if self.ds != None:
            self.ds.print(numOfIndents)

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     self.d.semantic(symbolTableGlobal, symbolTableLocal)
    #     if self.ds != None:
    #         self.ds.semantic(symbolTableGlobal, symbolTableLocal)

    def semantic(self, symTable, globalSymTable, indx):
        self.d.semantic(symTable, globalSymTable, indx)
        if self.ds != None:
            self.ds.semantic(symTable, globalSymTable, indx)