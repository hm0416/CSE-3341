import Core
import Term
import Factor

class Term:
    #potential children
    global factorNonTerm
    global termNonTerm

    #no error checking needed here
    def parse(self, S):
        factorNonTerm = Factor()
        factorNonTerm.parse(S)

        if S.currentToken() == Core.MULT:
            S.nextToken()
            termNonTerm = Term()
            termNonTerm.parse(S)

    def print(self):
        print("program")



