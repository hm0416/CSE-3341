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
            print("ERROR: Token should be ';', token should NOT be a " + S.currentToken().name)
            quit()
        S.nextToken()

    def print(self, numIndents):
        print(("\t" * numIndents) + "ref ", end = '')
        self.idL.print(0)
        print(";")

