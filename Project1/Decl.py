from Core import Core
from DeclInt import DeclInt
from DeclClass import DeclClass

class Decl:

    def __int__(self):
        self.dInt = None
        self.dClass = None
        self.whichStr = ""

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.INT:
            self.whichStr = "int"
            self.dInt = DeclInt()
            self.dInt.parse(S)
        elif S.currentToken() == Core.REF:
            self.whichString = "ref"
            self.dClass = DeclClass()
            self.dClass.parse(S)

        if S.currentToken() != Core.SEMICOLON:
            print("ERROR: Token should be ';'")
            quit()
        S.nextToken()


    def print(self):
        if self.whichStr == "int":
            self.dInt.print() #indent by 1
        elif self.whichStr == "ref":
            self.dClass.print() #has to be there
