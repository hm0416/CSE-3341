from Formals import Formals
from StmtSeq import StmtSeq
from Id import Id
from Core import Core
import globals
from Executor import Executor

class FuncDecl:

    def parse(self, parser):
        self.funcName = Id() #gets the name of the function that's being decalred
        self.funcName.parse(parser)
        globals.funcDeclName = self.funcName.identifier #gets name of declared function so can use with error message
        parser.expectedToken(Core.LPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.REF)
        parser.scanner.nextToken()
        self.formalParams = Formals() #gets the formal parameters of the declared function
        self.formalParams.parse(parser)
        # globals.listOfFuncParams.append(self.formalParams.id.identifier)
        # globals.formals = self.formalParams #stores the formal parameters
        parser.expectedToken(Core.RPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.BEGIN)
        parser.scanner.nextToken()
        self.funcBody = StmtSeq() #gets func body of the function that's being declared
        self.funcBody.parse(parser)
        # globals.bod = self.funcBody #stores the body of the function
        parser.expectedToken(Core.ENDFUNC)
        parser.scanner.nextToken()

    def semantic(self, executor):
        # fd = executor.func.get(self.funcName.identifier) #gets string name of func
        # formalParams = fd.formalParams #tree structure
        # fpList = formalParams.getAllParams()
        # print(fpList)
        # if len(fpList) != len(set(fpList)): #got this line of code from https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/
        #     print("SEMANTIC ERROR: Function formal parameters are not distinct from each other.")
        #     quit()
        if self.funcName.identifier in executor.func:
            print("ERROR: A function with name '" + self.funcName.identifier + "' has already been declared. Overloading not allowed.")
            quit()

    def execute(self, executor):
        self.semantic(executor) #checks for semantic errors
        # sets the function name to its definition - the self keyword gets all of the self declared variables in the parse function
        funcNameStr = self.funcName.getString()
        executor.func[funcNameStr] = self
        fd = executor.func.get(self.funcName.identifier)  # gets string name of func
        formalParams = fd.formalParams  # tree structure
        fpList = formalParams.getAllParams()
        if len(fpList) != len(set(
                fpList)):  # got this line of code from https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/
            print("SEMANTIC ERROR: Function formal parameters are not distinct from each other.")
            quit()
