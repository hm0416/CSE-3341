from Formals import Formals
from Id import Id
from Core import Core

class FuncCall:
	
    def parse(self, parser):
        parser.scanner.nextToken()
        self.funcName = Id()
        self.funcName.parse(parser)
        parser.expectedToken(Core.LPAREN)
        parser.scanner.nextToken()
        self.actualParams = Formals()
        self.actualParams.parse(parser)
        parser.expectedToken(Core.RPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.SEMICOLON)
        parser.scanner.nextToken()
	
    def print(self, indent):
        for x in range(indent):
            print("  ", end='')
        self.name.print()
        print("(", end='')
        self.actualParams.print()
        print(");\n", end='')

    def execute(self, executor):
        formalParams = executor.getFormalParams(self.funcName)
        body = executor.getBody(self.funcName)
        executor.pushFrame(formalParams, self.actualParams)
        body.execute(executor)
        executor.popFrame()
        executor.counter = executor.counter - 1 #decrement number of references because function popped off and variables have gone out of scope
        print("gc:" + str(executor.counter))
