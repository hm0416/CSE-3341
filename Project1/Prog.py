import Core
import DeclSeq
import StmtSeq

class Prog:
    global ds
    global ss

    # def __init__(self):

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.PROGRAM:
            print("ERROR")
            quit()
        S.nextToken() #scanner starts at declSeq
        if S.currentToken() == Core.INT or S.currentToken() == Core.REF:
            ds = DeclSeq() # this class will handle the consuming of toks
            ds.parse(S) #consume all toks that make up declSeq

        if S.currentToken() != Core.BEGIN:
            print("ERROR")
            quit()
        S.nextToken()
        ss = StmtSeq()
        ss.parse(S)

        if S.currentToken() != Core.END:
            print("ERROR")
            quit()
        S.nextToken()
        if S.currentToken() != Core.EOF:
            print("ERROR")
            quit()
        S.nextToken()

    def print(self):
        print("program")
        if ds != None:
            ds.print() #indent by 1
        print("begin")
        ss.print() #has to be there
        print("end")