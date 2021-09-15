import Core
import DeclInt
import DeclClass

class Decl:
    global dInt
    global dClass

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.INT:
            dInt = DeclInt()
            dInt.parse(S)
        elif S.currentToken() == Core.REF:
            dClass = DeclClass()
            dClass.parse(S)

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