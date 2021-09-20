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

    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"
            i += 1
        return tab

    def print(self, numIndents):
        # numIndents = self.createIndents(numOfIndents)
        print(("\t" * numIndents) + "ref ", end = '')
        self.idL.print(0)
        print(";")