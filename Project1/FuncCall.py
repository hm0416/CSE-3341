from Core import Core
from Executor import CoreVar
from Formals import Formals
from Id import Id
import globals


class FuncCall:
    def parse(self, parser):
        parser.expectedToken(Core.BEGIN)
        parser.scanner.nextToken()
        self.id = Id() #name of function to be called
        self.id.parse(parser)
        parser.expectedToken(Core.LPAREN)
        parser.scanner.nextToken()
        self.actualParams = Formals() #parameters that get passed to the function that's being called
        self.actualParams.parse(parser)
        parser.expectedToken(Core.RPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.SEMICOLON)
        parser.scanner.nextToken()

    def semantic(self, executor, fpList):
        # if len(fpList) != len(set(fpList)): #got this line of code from https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/
        #     print("SEMANTIC ERROR: Function formal parameters are not distinct from each other.")
        #     quit()
        # if not(self.id.identifier in executor.func):
        #     print("SEMANTIC ERROR: Function being called has not been declared/function call has no target.")
        #     quit()
        if (range(len(self.actualParams.getAllParams()))) != range(len(fpList)):
            print("SEMANTIC ERROR: Function being called does not match the number of arguments as the function declaration.")
            quit()

    def execute(self, executor):
        if self.id.identifier in executor.func:
            fd = executor.func.get(self.id.identifier) #gets string name of func

            formalParams = fd.formalParams #tree structure
            fpList = formalParams.getAllParams()
            # formalParams = globals.formals.getAllParams() #gets all formals by calling the getAllParams function in the Formals class
            # print(formalParams)

            actualParams = self.actualParams.getAllParams() #gets all the actual params

            self.semantic(executor, fpList) #checks for semantic errors

            for item in fpList:
                #gets index of each parameter in the list of formal parameters
                indexOfParam = fpList.index(item)
                #sets the type to REF, CoreVar has type and value as fields
                heapIndex = CoreVar(Core.REF)
                #for each formal param, find the corresponding actual param on the stack or static and get its value/look up what the values are
                #searches stack first then static
                heapIndex.value = executor.getStackOrStatic(actualParams[indexOfParam]).value
                # sets the formal param value to a index into the heap. the index corresponds to the actual param value
                executor.stackFrame[fpList[indexOfParam]] = heapIndex

            executor.stackSpace.append(executor.stackFrame) #new frame gets pushed to the stack space
            body = executor.func.get(self.id.identifier)
            body.funcBody.execute(executor)
            # globals.bod.execute(executor) #function body gets executed
            executor.stackSpace.pop() #pop frame off so main is the only frame left
        else:
            print("SEMANTIC ERROR: Function being called has not been declared/function call has no target.")
            quit()
