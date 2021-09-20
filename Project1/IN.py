from Core import Core


class IN:
    def __init__(self):
        self.identifier = ""

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.INPUT:
            S.nextToken()
        if S.currentToken() == Core.ID:
            self.identifier = S.getID()
            S.nextToken()

        if S.currentToken() != Core.SEMICOLON:
            print("ERROR: Token should be ';'")
            quit()
        S.nextToken()

    def createIndents(self, numOfIndents):
        tab = ""
        i = 0
        while i < numOfIndents:
            tab += "\t"

        return tab

    def print(self, numOfIndents):
        numIndents = "\t"
        print(numIndents + "input ", end = '')
        print(self.identifier + ";")