from Core import Core
from DeclInt import DeclInt
from DeclClass import DeclClass

class Decl:

    def __init__(self):
        self.dInt = None
        self.dClass = None
        self.whichStr = ""

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.INT:
            self.whichStr = "int"
            self.dInt = DeclInt()
            self.dInt.parse(S)
        elif S.currentToken() == Core.REF:
            self.whichStr = "ref"
            self.dClass = DeclClass()
            self.dClass.parse(S)


    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"

        return tab

    def print(self, numOfIndents):
        numIndents = self.createIndents(numOfIndents)
        if self.whichStr == "int":
            self.dInt.print(0) #indent by 1
        elif self.whichStr == "ref":
            self.dClass.print(0) #has to be there
