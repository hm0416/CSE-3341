from Formals import Formals
from StmtSeq import StmtSeq
from Id import Id
from Core import Core
import globals
from Executor import Executor

class FuncDecl:

    def parse(self, parser):
        #gets func name
        self.funcName = Id()
        self.funcName.parse(parser)
        parser.expectedToken(Core.LPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.REF)
        parser.scanner.nextToken()
        self.formalParams = Formals()
        self.formalParams.parse(parser)
        globals.formals = self.formalParams
        parser.expectedToken(Core.RPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.BEGIN)
        parser.scanner.nextToken()
        #gets func body
        self.funcBody = StmtSeq()
        self.funcBody.parse(parser)
        globals.bod = self.funcBody
        parser.expectedToken(Core.ENDFUNC)
        parser.scanner.nextToken()

    # sets the function name to its definition - the self keyword gets all of the self declared variables in the parse function
    def execute(self, executor):
        executor.func[self.funcName.getString()] = self