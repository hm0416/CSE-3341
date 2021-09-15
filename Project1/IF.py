import Core
import Cond
import StmtSeq

class IF:
    global condNonTerm
    global ss

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.IF:
            print("ERROR")
            quit()
        S.nextToken()
        condNonTerm = Cond()
        condNonTerm.parse(S)

        if S.currentToken() == Core.THEN:
            S.nextToken()
        ss = StmtSeq()
        ss.parse(S)

        if S.currentToken() == Core.ELSE:
            S.nextToken()
            ss = StmtSeq()
            ss.parse(S)
        if S.currentToken() == Core.ENDIF:
            S.nextToken()

    def print(self):
        print("program")
        if ds != None:
            ds.print(1) #indent by 1
        print("begin")
        ss.print(1) #has to be there
        print("end")