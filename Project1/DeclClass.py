from Core import Core
from IdList import IdList


class DeclClass:
    def __init__(self):
        self.idL = None

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.REF:
            print("ERROR: Token should be 'ref'")
            quit()
        S.nextToken()
        self.idL = IdList()
        self.idL.parse(S)
        if S.currentToken() != Core.SEMICOLON:
            print("ERROR: Token should be ';'")
            quit()
        S.nextToken()

    def print(self, numIndents):
        print(("\t" * numIndents) + "ref ", end = '')
        self.idL.print(0)
        print(";")

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     symbolTableGlobal.append("ref")
    #     self.idL.semantic(symbolTableGlobal, symbolTableLocal)

    def semantic(self, symTable, globalSymTable, indx):
        ele = symTable[indx]
        ele[self.idL.getIdentifier()] = "ref"
        self.idL.semantic(symTable, globalSymTable)
