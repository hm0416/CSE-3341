from Core import Core

class IdList:
    def __init__(self):
        self.idL = None
        self.identifier = ""
        self.whichStr = 0 #0 for none, 1 for comma

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.ID:
            print("ERROR: Token should be 'id'")
            quit()
        self.identifier = S.getID()
        S.nextToken()

        if S.currentToken() == Core.COMMA:
            self.whichStr = 1
            S.nextToken()
            self.idL = IdList()
            self.idL.parse(S)

    def print(self):
        print(self.identifier, end = '')
        if self.whichStr == 1:
            print(", ", end = '')
            self.idL.print()