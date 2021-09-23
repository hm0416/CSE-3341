from Core import Core


class IN:
    def __init__(self):
        self.identifier = ""

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.INPUT:
            S.nextToken()
        else:
            print("ERROR: Token should be 'input'")
            quit()
        if S.currentToken() == Core.ID:
            self.identifier = S.getID()
            S.nextToken()
        else:
            print("ERROR: Token should be an 'id'")
            quit()

        if S.currentToken() != Core.SEMICOLON:
            print("ERROR: Token should be ';'")
            quit()
        S.nextToken()

    def print(self, numIndents):
        print(("\t" * numIndents) + "input ", end = '')
        print(self.identifier + ";")

