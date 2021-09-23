from Core import Core


class Factor:
    def __init__(self):
        self.exprNonTerm = None
        self.identifier = ""
        self.const = 0
        self.whichStr = 0 #0 for none, 1 for ID, 2 for CONST

    def parse(self, S):
        if S.currentToken() == Core.ID:
            self.identifier = S.getID()
            self.whichStr = 1
            S.nextToken()
        elif S.currentToken() == Core.CONST:
            self.const = S.getCONST()
            self.whichStr = 2
            S.nextToken()
        elif S.currentToken() == Core.LPAREN:
            S.nextToken()
            from Expr import Expr
            self.exprNonTerm = Expr()
            self.exprNonTerm.parse(S)
            if S.currentToken() == Core.RPAREN:
                S.nextToken()
            else:
                print("ERROR: Right parenthesis is missing")
                quit()

    def print(self, numOfIndents):
        if self.whichStr == 1:
            print(self.identifier, end = '')
        elif self.whichStr == 2:
            print(self.const, end = '')
        elif self.exprNonTerm != None:
            print("(", end = '')
            self.exprNonTerm.print(0)
            print(")", end = '')

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     if self.whichStr == 1:
    #         symbolTableLocal.append(self.identifier)
    #     elif self.whichStr == 2:
    #         symbolTableLocal.append(self.const)
    #     elif self.exprNonTerm != None:
    #         symbolTableLocal.append("(")
    #         self.exprNonTerm.semantic(symbolTableGlobal, symbolTableLocal)
    #         symbolTableLocal.append(")")

    def semantic(self, symTable, globalSymTable):
        inScope = any(self.identifier in d for d in symTable)
        if inScope == False:
            print("ERROR: Variable " + self.identifier + " is not declared.")
            quit()

        # if self.whichStr == 1:
        #     if self.identifier not in globalSymTable:
        #         for ele in symTable:
        #             if self.identifier not in ele:
        #                 print("ERROR: Variable " + self.identifier + " is not declared.")
        #                 quit()
                                # elif self.whichStr == 2:
        #     local[self.identifier] = "const"
        if self.exprNonTerm != None:
            self.exprNonTerm.semantic(symTable, globalSymTable)
