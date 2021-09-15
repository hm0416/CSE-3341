import Core
import Expr


class Assign:
    global exprNonTerm

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.ID:
            print("ERROR")
            quit()
        S.nextToken()

        if S.currentToken() == Core.ASSIGN:
            S.nextToken()
            if S.currentToken() != Core.NEW or S.currentToken() != Core.REF:
                exprNonTerm = Expr()
                exprNonTerm.parse(S)

        if S.currentToken() == Core.NEW:
            S.nextToken()
        if S.currentToken() == Core.REF:
            S.nextToken()

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