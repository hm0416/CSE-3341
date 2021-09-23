from Core import Core


class IdList:
    def __init__(self):
        self.idL = None
        self.identifier = ""
        self.comma = 0 #0 for no comma, 1 for comma

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.ID:
            print("ERROR: Token should be 'id'")
            quit()
        self.identifier = S.getID()
        S.nextToken()

        if S.currentToken() == Core.COMMA:
            self.comma = 1
            S.nextToken()
            self.idL = IdList()
            self.idL.parse(S)

    def print(self, numIndents):
        print(("\t" * numIndents) + self.identifier, end = '')
        if self.idL != None:
            print(",", end = '')
            self.idL.print(0)

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     # symbolTableGlobal.append(self.identifier)
    #     # symbolTableGlobal[self.identifier] = "int"
    #     if self.idL != None:
    #         symbolTableGlobal.append(",")
    #         self.idL.semantic(symbolTableGlobal, symbolTableLocal)

    def semantic(self, symTable, globalSymTable):
        if self.idL != None:
            self.idL.semantic(symTable, globalSymTable)

    def getIdentifier(self):
        return self.identifier

    def isComma(self):
        return self.comma