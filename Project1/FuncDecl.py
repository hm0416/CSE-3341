from Formals import Formals
from StmtSeq import StmtSeq
from Id import Id
from Core import Core

class FuncDecl:
	
    def parse(self, parser):
        self.name = Id()
        self.name.parse(parser)
        parser.expectedToken(Core.LPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.REF)
        parser.scanner.nextToken()
        self.formalParams = Formals()
        self.formalParams.parse(parser)
        parser.expectedToken(Core.RPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.BEGIN)
        parser.scanner.nextToken()
        self.body = StmtSeq()
        self.body.parse(parser)
        parser.expectedToken(Core.ENDFUNC)
        parser.scanner.nextToken()
	
    def print(self, indent):
        for x in range(indent):
            print("  ", end='')
        self.name.print()
        print("(ref ", end='')
        self.formalParams.print()
        print(") begin\n", end='')
        self.body.print(indent+1)
        for x in range(indent):
            print("  ", end='')
        print("endfunc", end='')

    def execute(self, executor):
        executor.storeFuncDef(self.name, self)
        # executor.counter = executor.counter - 1 #decrement number of references because function popped off and variables have gone out of scope
        # print("gc:" + str(executor.counter))

    def getFormalParams(self):
        return self.formalParams

    def getBody(self):
        return self.body