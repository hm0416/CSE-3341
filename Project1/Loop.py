from Core import Core
from Cond import Cond
import StmtSeq

class Loop:
    # global condNonTerm
    # global ss

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.WHILE:
            print("ERROR")
            quit()
        S.nextToken()
        condNonTerm = Cond()
        condNonTerm.parse(S)

        if S.currentToken() == Core.BEGIN:
            S.nextToken()
        ss = StmtSeq()
        ss.parse(S)

        if S.currentToken() == Core.ENDWHILE:
            S.nextToken()

    # def print(self):
    #     print("program")
    #     if ds != None:
    #         ds.print(1) #indent by 1
    #     print("begin")
    #     ss.print(1) #has to be there
    #     print("end")