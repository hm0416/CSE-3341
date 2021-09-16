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
            self.assignNonTerm.parse(S)
        if S.currentToken() == Core.OUTPUT:
            self.outputNonTerm = OUT()
            self.outputNonTerm.parse(S)
        if S.currentToken() == Core.INT or S.currentToken == Core.REF:
            self.declNonTerm = Decl()
            self.declNonTerm.parse(S)

    def print(self):
        self.assignNonTerm.print()
        self.ifNonTerm.print()
        self.inputNonTerm.print()
        self.outputNonTerm.print()
        self.loopNonTerm.print()
        self.declNonTerm.print()