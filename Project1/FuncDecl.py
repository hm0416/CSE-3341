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

    def semantic(self, executor):
        if self.funcName.identifier in executor.func:
            print("ERROR: A function with name '" + self.funcName.identifier + "' has already been declared. Overloading not allowed.")
            quit()

    # sets the function name to its definition - the self keyword gets all of the self declared variables in the parse function
    def execute(self, executor):
        # if not hasattr(self, 'funcBody'):
        #     print("ERROR: Function body missing (no stmt-seq)")
        #     quit()
        # else:
        self.semantic(executor)
        executor.func[self.funcName.getString()] = self