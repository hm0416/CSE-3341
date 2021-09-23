from Core import Core
from IdList import IdList

class DeclInt:
    def __init__(self):
        self.idL = None

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.INT:
            print("ERROR: Token should be 'int'")
            quit()
        S.nextToken()
        self.idL = IdList()
        self.idL.parse(S)
        if S.currentToken() != Core.SEMICOLON:
            print("ERROR: Token should be ';'")
            quit()
        S.nextToken()

    def print(self, numIndents):
        print(("\t" * numIndents) + "int ", end = '')
        self.idL.print(0)
        print(";")

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     symbolTableGlobal.append("int")
    #     self.idL.semantic(symbolTableGlobal, symbolTableLocal)

    def semantic(self, symTable, globalSymTable, indx):
        dict = symTable[indx]
        dict[self.idL.getIdentifier()] = "int"
        # if self.idL.isComma() == 1:
        #     globalSymTable[self.idL.getIdentifier()] = "int"
        self.idL.semantic(symTable, globalSymTable)
