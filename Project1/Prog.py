from Core import Core
from DeclSeq import DeclSeq
from StmtSeq import StmtSeq

class Prog:
    def __init__(self):
        self.ds = None
        self.ss = None

    def parse(self, S): #should not output anything unless error case
        if S.currentToken() != Core.PROGRAM:
            print("ERROR: Token should be 'program'")
            quit()
        S.nextToken() #scanner starts at declSeq

        if S.currentToken() == Core.BEGIN:
            S.nextToken()
        else:
            self.ds = DeclSeq() # this class will handle the consuming of toks
            self.ds.parse(S) #consume all toks that make up declSeq
        self.ss = StmtSeq()
        self.ss.parse(S)

        if S.currentToken() != Core.END:
            print("ERROR: Token should be 'end'")
            quit()
        S.nextToken()
        if S.currentToken() != Core.EOF:
            print("ERROR: Program should be at the end of the file")
            quit()
        S.nextToken()

    def print(self, numOfIndents):
        print("program")
        if self.ds != None:
            self.ds.print(numOfIndents) #indent by 1
        print("begin")
        self.ss.print(numOfIndents) #has to be there
        print("end")

    # def semantic(self, symbolTableGlobal, symbolTableLocal):
    #     if self.ds != None:
    #         self.ds.semantic(symbolTableGlobal, symbolTableLocal)
    #     self.ss.semantic(symbolTableGlobal, symbolTableLocal)

    def semantic(self, symTable, globalSymTable):
        indx = 0
        symTable.append({}) #new scope - local
        if self.ds != None:
            self.ds.semantic(symTable, globalSymTable, indx)
        self.ss.semantic(symTable, globalSymTable, indx)

