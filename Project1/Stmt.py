from Core import Core
from Decl import Decl
from Assign import Assign
from Loop import Loop
from OUT import OUT
from IN import IN
from IF import IF


class Stmt:
    def __init__(self):
        self.assignNonTerm = None
        self.ifNonTerm = None
        self.inputNonTerm = None
        self.outputNonTerm = None
        self.loopNonTerm = None
        self.declNonTerm = None

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.ID:
            self.assignNonTerm = Assign()
            self.assignNonTerm.parse(S)
        if S.currentToken() == Core.IF:
            self.ifNonTerm = IF()
            self.ifNonTerm.parse(S)
        if S.currentToken() == Core.WHILE:
            self.loopNonTerm = Loop()
            self.loopNonTerm.parse(S)
        if S.currentToken() == Core.INPUT:
            self.inputNonTerm = IN()
            self.inputNonTerm.parse(S)
        if S.currentToken() == Core.OUTPUT:
            self.outputNonTerm = OUT()
            self.outputNonTerm.parse(S)
        if S.currentToken() == Core.INT or S.currentToken() == Core.REF:
            self.declNonTerm = Decl()
            self.declNonTerm.parse(S)

    def print(self, numOfIndents):
        if self.assignNonTerm != None:
            self.assignNonTerm.print(numOfIndents)
        if self.ifNonTerm != None:
            self.ifNonTerm.print(numOfIndents)
        if self.loopNonTerm != None:
            self.loopNonTerm.print(numOfIndents)
        if self.inputNonTerm != None:
            self.inputNonTerm.print(numOfIndents)
        if self.outputNonTerm != None:
            self.outputNonTerm.print(numOfIndents)
        if self.declNonTerm != None:
            self.declNonTerm.print(numOfIndents)