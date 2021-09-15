import Expr
import Core

class Cmpr:
    global exprNonTerm

    def parse(self, S): #should not output anything unless error case
        exprNonTerm = Expr()
        exprNonTerm.parse(S)
        if S.currentToken() == Core.EQUAL:
            S.nextToken()
            exprNonTerm = Expr()
            exprNonTerm.parse(S)
        elif S.currentToken() == Core.LESS:
            S.nextToken()
            exprNonTerm = Expr()
            exprNonTerm.parse(S)
        elif S.currentToken() == Core.LESSEQUAL:
            S.nextToken()
            exprNonTerm = Expr()
            exprNonTerm.parse(S)

    def print(self):
        print("program")
        if ds != None:
            ds.print(1) #indent by 1
        print("begin")
        ss.print(1) #has to be there
        print("end")