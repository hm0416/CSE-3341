from Core import Core
from Executor import CoreVar
from Formals import Formals
from Id import Id
import globals


class FuncCall:
    def parse(self, parser):
        parser.expectedToken(Core.BEGIN)
        parser.scanner.nextToken()
        self.id = Id()
        self.id.parse(parser)
        parser.expectedToken(Core.LPAREN)
        parser.scanner.nextToken()
        self.actualParams = Formals()
        self.actualParams.parse(parser)
        parser.expectedToken(Core.RPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.SEMICOLON)
        parser.scanner.nextToken()

    def semantic(self, executor):
        # if not(self.id.identifier in executor.func) or (range(len(self.actualParams.execute(self)) != range(len(globals.formals.execute(self))))):
        #     print("SEMANTIC ERROR: Function being called has not been declared/function call has no target.")
        #     quit()
        if not(self.id.identifier in executor.func):
            print("SEMANTIC ERROR: Function being called has not been declared/function call has no target.")
            quit()

    def execute(self, executor):
        self.semantic(executor) #checks for semantic errors
        formalParams = globals.formals.getAllParams(self) #gets all formals by calling the execute function in the Formals class
        actualParams = self.actualParams.getAllParams(self) #gets all the actual params

        for i in range(len(formalParams)):
            #sets the type to REF
            heapIndex = CoreVar(Core.REF)
            #for each formal param, find the corresponding actual param on the stack or static and get its value
            heapIndex.value = executor.getStackOrStatic(actualParams[i]).value
            # sets the formal param value to a index into the heap. the index corresponds to the actual param value
            executor.stackFrame[formalParams[i]] = heapIndex

        executor.stackSpace.append(executor.stackFrame) #new frame gets appended to the stack space
        globals.bod.execute(executor) #function body gets executed
