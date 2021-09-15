from string import whitespace, ascii_letters, digits
from Core import Core

class Scanner:

    def __init__(self, text_stream):
        # Create a scanner from an opened text stream
        self._ts = open(text_stream, 'r')
        self._curr_pos = self._ts.tell()
        self._prev_pos = None
        self._buffer = None
        self.token = None
        self.id = None
        self.const = None
        self.nextToken()

    def reset(self):
        self._ts.seek(0)

    def readChar(self):
        char = self._ts.read(1)
        self._prev_pos = self._curr_pos
        self._curr_pos = self._ts.tell()
        return char

    def pushChar(self):
        self._ts.seek(self._prev_pos)
        self._curr_pos = self._prev_pos
        self._prev_pos = None

    def errrorMessage(self, badThing):
        print("ERROR: Invalid character or constant: " + badThing)
        self.token=Core.ERROR

    def nextToken(self):
        c = self.readChar()
        # Skip all whitespaces
        while c in whitespace and c!="":
            c = self.readChar()

        # Handle the end of the stream
        if c=="":
            self.token = Core.EOF
        elif c in ascii_letters:
            tokString=""
            while (c in ascii_letters or c in digits) and c!="":
                tokString+=c
                c=self.readChar()
            self.pushChar()
            if tokString=="program":
                self.token=Core.PROGRAM
            elif tokString=="begin":
                self.token=Core.BEGIN
            elif tokString=="end":
                self.token=Core.END
            elif tokString=="new":
                self.token=Core.NEW
            elif tokString=="define":
                self.token=Core.DEFINE
            elif tokString=="extends":
                self.token=Core.EXTENDS
            elif tokString=="class":
                self.token=Core.CLASS
            elif tokString=="endclass":
                self.token=Core.ENDCLASS
            elif tokString=="int":
                self.token=Core.INT
            elif tokString=="endfunc":
                self.token=Core.ENDFUNC
            elif tokString=="if":
                self.token=Core.IF
            elif tokString=="then":
                self.token=Core.THEN
            elif tokString=="else":
                self.token=Core.ELSE
            elif tokString=="while":
                self.token=Core.WHILE
            elif tokString=="endwhile":
                self.token=Core.ENDWHILE
            elif tokString=="endif":
                self.token=Core.ENDIF
            elif tokString=="input":
                self.token=Core.INPUT
            elif tokString=="output":
                self.token=Core.OUTPUT
            else:
                self.token=Core.ID
                self.id=tokString
        elif c in digits:
            tokString=""
            while c in digits and c!="":
                tokString+=c
                c=self.readChar()
            self.pushChar()
            self.const = int(tokString)
            self.token=Core.CONST
            if self.const > 1023:
                self.errrorMessage(tokString)
        elif c==';':
            self.token = Core.SEMICOLON
        elif c=='(':
            self.token = Core.LPAREN
        elif c==')':
            self.token = Core.RPAREN
        elif c==',':
            self.token = Core.COMMA
        elif c=='!':
            self.token = Core.NEGATION
        elif c=='+':
            self.token = Core.ADD
        elif c=='-':
            self.token = Core.SUB
        elif c=='*':
            self.token = Core.MULT
        elif c=='=':
            nextChar = self.readChar()
            if nextChar=='=':
                self.token=Core.EQUAL
            else:
                self.pushChar()
                self.token=Core.ASSIGN
        elif c=='<':
            nextChar = self.readChar()
            if nextChar=='=':
                self.token=Core.LESSEQUAL
            else:
                self.pushChar()
                self.token=Core.LESS
        else:
            self.errrorMessage(c)
        
    def currentToken(self):
        return self.token

    def getID(self):
        return self.id

    def getCONST(self):
        return self.const