import Scanner
import Core

class Parser:
    def __init__(self, filename):
        self.scan = Scanner(filename)
        self.currentTok = self.scan.nextToken(filename)

    def progParse(self, filename, tokensList):
        if self.currentToken(tokensList).name == Core.PROGRAM:
            self.nextToken(filename)
        else:
            print("ERROR: First token should be 'program'")
        self.declSeq()

        if self.currentToken(tokensList).name == Core.BEGIN:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'begin'")
        self.stmtSeq()

        if self.currentToken(tokensList).name == Core.END:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'end'")

    def declSeq(self, filename, tokensList):
        self.decl(filename, tokensList)
        self.declSeq(filename, tokensList)


