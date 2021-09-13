import Scanner
import Core

class Parser:
    def __init__(self, filename):
        self.scan = Scanner(filename)
        self.currentTok = self.scan.nextToken(filename)

class Prog:
    def __init__(self):
        self.dSeq = None
        self.sSeq = None

    def progParse(self, filename, tokensList):
        # curr = self.currentTok
        self.declSeq()

        if self.currentToken() == Core.PROGRAM:
            self.nextToken(filename)
            self.progParse()
        else:
            print("ERROR: First token should be 'program'")

# class Decl-seq:
#     def DeclSeqParse(self):
#         return 0
#
# class Stmt-seq:
#
# class Decl:

