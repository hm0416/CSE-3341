import Core
import Cond
import Cmpr

class Cond:
    global condNonTerm
    global cmprNonTerm

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() == Core.NEGATION:
            S.nextToken()
            if S.currentToken() == Core.LPAREN:
                S.nextToken()
                condNonTerm = Cond()
                condNonTerm.parse(S)
                if S.currentToken() == Core.RPAREN:
                    S.nextToken()

        if S.currentToken() != Core.NEGATION:
            cmprNonTerm = Cmpr()
            cmprNonTerm.parse(S)
            if S.currentToken() == Core.OR:
                S.nextToken()
                condNonTerm = Cond()
                condNonTerm.parse(S)

    def print(self):
        print("program")
        if ds != None:
            ds.print(1) #indent by 1
        print("begin")
        ss.print(1) #has to be there
        print("end")