import Scanner
import Core

class Parser:
    def __init__(self, filename):
        self.scan = Scanner(filename)
        self.currentTok = self.scan.nextToken(filename)

    def progParse(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.PROGRAM:
            self.nextToken(filename)
            if self.scan.currentToken(tokensList) != Core.BEGIN:
                self.declSeq()
        else:
            print("ERROR: First token should be 'program'")

        if self.scan.currentToken(tokensList) == Core.BEGIN:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'begin'")
        self.stmtSeq()

        if self.scan.currentToken(tokensList) == Core.END:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'end'")

    def declSeq(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.INT or self.scan.currentToken(tokensList) == Core.REF:
            self.decl(filename, tokensList)
        else:
            self.decl(filename, tokensList)
            self.declSeq(filename, tokensList)

    def stmtSeq(self, filename, tokensList):

        self.decl(filename, tokensList)
        self.declSeq(filename, tokensList)

    def decl(self, filename, tokensList):
        self.declInt(filename, tokensList)
        self.declClass(filename, tokensList)

    def declInt(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.INT:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'int'")
        self.idList(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be ';'")

    def declClass(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.REF:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'ref'")
        self.idList(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be ';'")

    def idList(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.ID:
            val = self.getID()
            self.nextToken(filename)
            if self.scan.currentToken(tokensList) == Core.COMMA:
                self.nextToken(filename)
                self.idList(filename, tokensList)
            else:
                print("ERROR: Token should be 'comma'")
        else:
            print("ERROR: Token should be 'id'")

    def stmt(self, filename, tokensList):
        self.decl(filename, tokensList)
        self.declSeq(filename, tokensList)

    def assign(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.ID:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'id'")

        if self.scan.currentToken(tokensList) == Core.ASSIGN:
            self.nextToken(filename)
            if self.scan.currentToken(tokensList) != Core.NEW or self.scan.currentToken(tokensList) != Core.REF:
                self.expr(filename, tokensList)
        else:
            print("ERROR: Token should be 'assign'")

        if self.scan.currentToken(tokensList) == Core.NEW:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'new'")

        if self.scan.currentToken(tokensList) == Core.REF:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'ref'")

        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be ';'")

    def IN(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.INPUT:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'input'")

        if self.scan.currentToken(tokensList) == Core.ID:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'id'")

        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be ';'")

    def OUT(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.OUTPUT:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'output'")
        self.expr(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be ';'")

    def IF(self, filename, tokensList):
        self.decl(filename, tokensList)
        self.declSeq(filename, tokensList)

    def loop(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.WHILE:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'while'")
        self.cond(filename, tokensList)

        if self.scan.currentToken(tokensList) == Core.BEGIN:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'begin'")
        self.stmtSeq(filename, tokensList)

        if self.scan.currentToken(tokensList) == Core.ENDWHILE:
            self.nextToken(filename)
        else:
            print("ERROR: Token should be 'endwhile'")

    def cond(self, filename, tokensList):
        self.decl(filename, tokensList)
        self.declSeq(filename, tokensList)

    def cmpr(self, filename, tokensList):
        self.expr(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.EQUAL:
            self.nextToken(filename)
            self.expr(filename, tokensList)
        elif self.scan.currentToken(tokensList) == Core.LESS:
            self.nextToken(filename)
            self.expr(filename, tokensList)
        elif self.scan.currentToken(tokensList) == Core.LESSEQUAL:
            self.nextToken(filename)
            self.expr(filename, tokensList)

    def expr(self, filename, tokensList):
        self.term(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.ADD:
            self.nextToken(filename)
            self.expr(filename, tokensList)
        elif self.scan.currentToken(tokensList) == Core.SUB:
            self.nextToken(filename)
            self.expr(filename, tokensList)

    def term(self, filename, tokensList):
        self.factor(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.MULT:
            self.nextToken(filename)
            self.term(filename, tokensList)

    def factor(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.ID:
            self.nextToken(filename)
        elif self.scan.currentToken(tokensList) == Core.CONST:
            self.nextToken(filename)
        elif self.scan.currentToken(tokensList) == Core.LPAREN:
            self.nextToken(filename)
            self.expr(filename, tokensList)
            if self.scan.currentToken(tokensList) == Core.RPAREN:
                self.nextToken(filename)




