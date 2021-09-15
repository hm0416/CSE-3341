import Core
import Assign
import Loop
import OUT
import IN
import Decl
import IF


class Stmt:
    global assignNonTerm
    global ifNonTerm
    global inputNonTerm
    global outputNonTerm
    global loopNonTerm
    global declNonTerm

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.ID:
            assignNonTerm = Assign()
            assignNonTerm.parse(S)
        if S.currentToken() == Core.IF:
            ifNonTerm = IF()
            ifNonTerm.parse(S)
        if S.currentToken() == Core.WHILE:
            loopNonTerm = Loop()
            loopNonTerm.parse(S)
        if S.currentToken()== Core.INPUT:
            inputNonTerm = IN()
            assignNonTerm.parse(S)
        if S.currentToken() == Core.OUTPUT:
            outputNonTerm = OUT()
            outputNonTerm.parse(S)
        if S.currentToken() == Core.INT or S.currentToken == Core.REF:
            declNonTerm = Decl()
            declNonTerm.parse(S)

    def print(self):
        print("program")
        if ds != None:
            ds.print(1) #indent by 1
        print("begin")
        ss.print(1) #has to be there
        print("end")