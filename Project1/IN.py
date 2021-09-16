from Core import Core


class IN:

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.INPUT:
            S.nextToken()
        if S.currentToken() == Core.ID:
            S.nextToken()

        if S.currentToken() != Core.SEMICOLON:
            print("ERROR: Token should be ';'")
            quit()
        S.nextToken()

    # def print(self):
    #     print("program")
    #     if ds != None:
    #         ds.print(1) #indent by 1
    #     print("begin")
    #     ss.print(1) #has to be there
    #     print("end")