import Core
import StmtSeq
import Stmt


class StmtSeq:
    global s
    global ss

    def parse(self, S): #should not output anything unless error case
        s = Stmt()
        s.parse(S)

        if S.currentToken == Core.ID or S.currentToken == Core.IF or S.currentToken == Core.WHILE or S.currentToken == Core.INPUT or S.currentToken == Core.OUTPUT or S.currentToken == Core.INT or S.currentToken == Core.REF:
            ss = StmtSeq() # this class will handle the consuming of toks
            ss.parse(S) #consume all toks that make up declSeq

    def print(self):
        print("program")
        if ds != None:
            ds.print(1) #indent by 1
        print("begin")
        ss.print(1) #has to be there
        print("end")