import Scanner
import Core
import ParseTree

class Parser:
    def __init__(self, filename, tokensList):
        self.scan = Scanner(filename)
        self.parseTree = ParseTree()
        self.currentTok = self.scan.nextToken(tokensList) #should return PROGRAM

    def progParse(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.PROGRAM:
            self.parseTree += "program"
            self.nextToken(tokensList)
        else:
            print("ERROR: First token should be 'program'")

        if self.scan.currentToken(tokensList) == Core.BEGIN:
            self.parseTree += "begin"
            self.nextToken(tokensList)
        else:
            self.declSeq(filename, tokensList)
            self.nextToken(tokensList)

        self.stmtSeq(filename, tokensList)

        if self.scan.currentToken(tokensList) == Core.END:
            self.parseTree += "end"
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'end'")

    def declSeq(self, filename, tokensList):
        self.decl(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.INT or self.scan.currentToken(tokensList) == Core.REF:
            self.declSeq(filename, tokensList)

    def stmtSeq(self, filename, tokensList):
        self.stmt(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.ID or self.scan.currentToken(tokensList) == Core.IF or self.scan.currentToken(tokensList) == Core.WHILE or self.scan.currentToken(tokensList) == Core.INPUT or self.scan.currentToken(tokensList) == Core.OUTPUT or self.scan.currentToken(tokensList) == Core.INT or self.scan.currentToken(tokensList) == Core.REF:
            self.stmtSeq(filename, tokensList)

    def decl(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.INT:
            self.declInt(filename, tokensList)
        elif self.scan.currentToken(tokensList) == Core.REF:
            self.declClass(filename, tokensList)

        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be ';'")

    def declInt(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.INT:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'int'")
        self.idList(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be ';'")

    def declClass(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.REF:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'ref'")
        self.idList(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be ';'")

    def idList(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.ID:
            val = self.getID()
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'id'")

        if self.scan.currentToken(tokensList) == Core.COMMA:
            self.nextToken(tokensList)
            self.idList(filename, tokensList)
        else:
            print("ERROR: Token should be 'comma'")

    def stmt(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.ID:
            self.assign(filename, tokensList)
        else:
            print("ERROR: Token should be 'id'")

        if self.scan.currentToken(tokensList) == Core.IF:
            self.IF(filename, tokensList)
        else:
            print("ERROR: Token should be 'if'")

        if self.scan.currentToken(tokensList) == Core.WHILE:
            self.loop(filename, tokensList)
        else:
            print("ERROR: Token should be 'while'")

        if self.scan.currentToken(tokensList) == Core.INPUT:
            self.IN(filename, tokensList)
        else:
            print("ERROR: Token should be 'input'")

        if self.scan.currentToken(tokensList) == Core.OUTPUT:
            self.OUT(filename, tokensList)
        else:
            print("ERROR: Token should be 'output'")

        if self.scan.currentToken(tokensList) == Core.INT or self.scan.currentToken(tokensList) == Core.REF:
            self.decl(filename, tokensList)
        else:
            print("ERROR: Token should be 'int or ref'")

    def assign(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.ID:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'id'")

        if self.scan.currentToken(tokensList) == Core.ASSIGN:
            self.nextToken(tokensList)
            if self.scan.currentToken(tokensList) != Core.NEW or self.scan.currentToken(tokensList) != Core.REF:
                self.expr(filename, tokensList)
        else:
            print("ERROR: Token should be 'assign'")

        if self.scan.currentToken(tokensList) == Core.NEW:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'new'")

        if self.scan.currentToken(tokensList) == Core.REF:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'ref'")

        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be ';'")

    def IN(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.INPUT:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'input'")

        if self.scan.currentToken(tokensList) == Core.ID:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'id'")

        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be ';'")

    def OUT(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.OUTPUT:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'output'")
        self.expr(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.SEMICOLON:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be ';'")

    def IF(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.IF:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'if'")
        self.cond(filename, tokensList)

        if self.scan.currentToken(tokensList) == Core.THEN:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'then'")
        self.stmtSeq(filename, tokensList)

        if self.scan.currentToken(tokensList) == Core.ELSE:
            self.nextToken(tokensList)
            self.stmtSeq(filename, tokensList)

        if self.scan.currentToken(tokensList) == Core.ENDIF:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'endif'")

    def loop(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.WHILE:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'while'")
        self.cond(filename, tokensList)

        if self.scan.currentToken(tokensList) == Core.BEGIN:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'begin'")
        self.stmtSeq(filename, tokensList)

        if self.scan.currentToken(tokensList) == Core.ENDWHILE:
            self.nextToken(tokensList)
        else:
            print("ERROR: Token should be 'endwhile'")

    def cond(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.NEGATION:
            self.nextToken(tokensList)
            if self.scan.currentToken(tokensList) == Core.LPAREN:
                self.nextToken(tokensList)
                self.cond(filename, tokensList)
                if self.scan.currentToken(tokensList) == Core.RPAREN:
                    self.nextToken(tokensList)
        else:
            print("ERROR: Token should be '!'")

        if self.scan.currentToken(tokensList) != Core.NEGATION:
            self.cmpr(filename, tokensList)
            if self.scan.currentToken(tokensList) == Core.OR:
                self.nextToken(tokensList)
                self.cond(filename, tokensList)
        else:
            print("ERROR: Token shouldn't be '!'")

    def cmpr(self, filename, tokensList):
        self.expr(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.EQUAL:
            self.nextToken(tokensList)
            self.expr(filename, tokensList)
        elif self.scan.currentToken(tokensList) == Core.LESS:
            self.nextToken(tokensList)
            self.expr(filename, tokensList)
        elif self.scan.currentToken(tokensList) == Core.LESSEQUAL:
            self.nextToken(tokensList)
            self.expr(filename, tokensList)

    def expr(self, filename, tokensList):
        self.term(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.ADD:
            self.nextToken(tokensList)
            self.expr(filename, tokensList)
        elif self.scan.currentToken(tokensList) == Core.SUB:
            self.nextToken(tokensList)
            self.expr(filename, tokensList)

    def term(self, filename, tokensList):
        self.factor(filename, tokensList)
        if self.scan.currentToken(tokensList) == Core.MULT:
            self.nextToken(tokensList)
            self.term(filename, tokensList)

    def factor(self, filename, tokensList):
        if self.scan.currentToken(tokensList) == Core.ID:
            self.nextToken(tokensList)
        elif self.scan.currentToken(tokensList) == Core.CONST:
            self.nextToken(tokensList)
        elif self.scan.currentToken(tokensList) == Core.LPAREN:
            self.nextToken(tokensList)
            self.expr(filename, tokensList)
            if self.scan.currentToken(tokensList) == Core.RPAREN:
                self.nextToken(tokensList)




