from Core import Core

class StmtSeq:
    def __init__(self):
        self.s = None
        self.ss = None

    def parse(self, S): #should not output anything unless error case
        self.s = Stmt()
        self.s.parse(S)

        if S.currentToken() == Core.ID or S.currentToken() == Core.IF or S.currentToken() == Core.WHILE or S.currentToken() == Core.INPUT or S.currentToken() == Core.OUTPUT or S.currentToken() == Core.INT or S.currentToken() == Core.REF:
            self.ss = StmtSeq() # this class will handle the consuming of toks
            self.ss.parse(S) #consume all toks that make up declSeq

    def print(self, numOfIndents):
        self.s.print(numOfIndents)
        if self.ss != None:
            self.ss.print(numOfIndents)

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     self.s.semantic(symbolTableGlobal, symbolTableLocal)
    #     if self.ss != None:
    #         self.ss.semantic(symbolTableGlobal, symbolTableLocal)

    def semantic(self, symTable, globalSymTable, indx):
        self.s.semantic(symTable, globalSymTable, indx)
        if self.ss != None:
            self.ss.semantic(symTable, globalSymTable, indx)

from Stmt import Stmt