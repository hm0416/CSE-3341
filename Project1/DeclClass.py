import Core
import IdList


class DeclClass:
    global idList

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.REF:
            print("ERROR: Token should be 'ref'")
            quit()
        S.nextToken()
        idL = IdList()
        idL.parse(S)
        if S.currentToken() != Core.SEMICOLON:
            print("ERROR: Token should be ';'")
            quit()
        S.nextToken()

    def print(self):
        print("program")
        if ds != None:
            ds.print(1) #indent by 1
        print("begin")
        ss.print(1) #has to be there
        print("end")