from Core import Core


class IdList:
    def __init__(self):
        self.idL = None
        self.identifier = ""
        self.comma = 0 #0 for no comma, 1 for comma

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.ID:
            print("ERROR: Token should be 'id', token should NOT be a " + S.currentToken().name)
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
