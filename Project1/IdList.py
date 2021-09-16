from Core import Core

class IdList:
    # global idList

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.ID:
            print("ERROR: Token should be 'id'")
            quit()
        #get value of ID
        S.nextToken()

        if S.currentToken() == Core.COMMA:
            S.nextToken()
            idL = IdList()
            idL.parse(S)

    # def print(self):
    #     print("program")
    #     if ds != None:
    #         ds.print(1) #indent by 1
    #     print("begin")
    #     ss.print(1) #has to be there
    #     print("end")