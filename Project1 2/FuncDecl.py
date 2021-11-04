from Formals import Formals
from StmtSeq import StmtSeq
from Id import Id
from Core import Core
from Executor import Executor

class FuncDecl:

    def parse(self, parser):
        self.funcName = Id() #gets the name of the function that's being decalred
        self.funcName.parse(parser)
        parser.expectedToken(Core.LPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.REF)
        parser.scanner.nextToken()
        self.formalParams = Formals() #gets the formal parameters of the declared function
        self.formalParams.parse(parser)
        parser.expectedToken(Core.RPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.BEGIN)
        parser.scanner.nextToken()
        self.funcBody = StmtSeq() #gets func body of the function that's being declared
        self.funcBody.parse(parser)
        parser.expectedToken(Core.ENDFUNC)
        parser.scanner.nextToken()

    def semantic(self, executor):
        if self.funcName.identifier in executor.func: #checks if function name already in the dict of functions
            print("ERROR: A function with name '" + self.funcName.identifier + "' has already been declared. Overloading not allowed.")
            quit()

    def execute(self, executor):
        self.semantic(executor) #checks for semantic errors
        funcNameStr = self.funcName.getString() #gets string versin of function name
        executor.func[funcNameStr] = self # sets the function name to its definition - the self keyword gets all of the self declared variables in the parse function

        fd = executor.func.get(self.funcName.identifier)  # gets string name of func, fd stands for funcDecl
        fParams = fd.formalParams  # tree structure
        fpList = fParams.getAllParams()  # list of formal parameters
        if len(fpList) != len(set(fpList)):  # got this line of code from https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/
            print("SEMANTIC ERROR: Function formal parameters are not distinct from each other.")
            quit()
