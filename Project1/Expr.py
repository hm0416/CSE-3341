from Core import Core
from Term import Term


class Expr:
    def __init__(self):
        self.term = None
        self.exprNonTerm = None
        self.operator = 0  # 0 if no operation, 1 if addition, 2 if subtraction

    def parse(self, S):
        self.term = Term()
        self.term.parse(S)

        if S.currentToken() == Core.ADD:
            S.nextToken()
            if S.currentToken() == Core.ADD:
                print("ERROR: Can't have ++")
                quit()
            self.operator = 1
            self.exprNonTerm = Expr()
            self.exprNonTerm.parse(S)
        elif S.currentToken() == Core.SUB:
            S.nextToken()
            if S.currentToken() == Core.SUB:
                print("ERROR: Can't have --")
                quit()
            self.operator = 2
            self.exprNonTerm = Expr()
            self.exprNonTerm.parse(S)

    def print(self, numOfIndents):
        self.term.print(1)
        if self.exprNonTerm != None:
            if self.operator == 1:
                print("+", end = '')
                self.exprNonTerm.print(0)
            elif self.operator == 2:
                print("-", end = '')
                self.exprNonTerm.print(0)

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     self.term.semantic(symbolTableGlobal, symbolTableLocal)
    #     if self.exprNonTerm != None:
    #         if self.operator == 1:
    #             symbolTableLocal.append("+")
    #             self.exprNonTerm.semantic(symbolTableGlobal, symbolTableLocal)
    #         elif self.operator == 2:
    #             symbolTableLocal.append("-")
    #             self.exprNonTerm.semantic(symbolTableGlobal, symbolTableLocal)

    def semantic(self, symTable, globalSymTable):
        self.term.semantic(symTable, globalSymTable)
        if self.exprNonTerm != None:
            if self.operator == 1:
                self.exprNonTerm.semantic(symTable, globalSymTable)
            elif self.operator == 2:
                self.exprNonTerm.semantic(symTable, globalSymTable)