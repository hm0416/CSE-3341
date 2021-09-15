import Core
import DeclSeq
import Decl


class DeclSeq:
    global d
    global ds

    def parse(self, S): #should not output anything unless error case
        d = Decl()
        d.parse(S)

        if S.currentToken == Core.BEGIN:
            S.nextToken()
        if S.currentToken == Core.INT or S.currentToken == Core.REF:
            ds = DeclSeq() # this class will handle the consuming of toks
            ds.parse(S) #consume all toks that make up declSeq

    def print(self):
        print("program")
        if ds != None:
            ds.print(1) #indent by 1
        print("begin")
        ss.print(1) #has to be there
        print("end")