from Core import Core
from Executor import CoreVar
from Formals import Formals
from Id import Id

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

    def semantic(self, fpList):
        if (range(len(self.actualParams.getAllParams()))) != range(len(fpList)): #checks if number of actual params == to # of formal params
            print("SEMANTIC ERROR: Function being called does not match the number of arguments as the function declaration.")
            quit()

    def execute(self, executor):
        if self.id.identifier in executor.func: #if the name of the function being called is declared then proceed, else throw an error
            fd = executor.func.get(self.id.identifier) #gets string name of func, fd stands for funcDecl
            fParams = fd.formalParams #tree structure
            fpList = fParams.getAllParams() #list of formal parameters
            actualParams = self.actualParams.getAllParams() #gets all the actual params

            self.semantic(fpList) #checks for semantic errors

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
            body = executor.func.get(self.id.identifier) #gets the tree structure for the body of specified function
            body.funcBody.execute(executor) #function body gets executed
            executor.stackSpace.pop() #pop frame off so main is the only frame left
        else:
            print("SEMANTIC ERROR: Function being called has not been declared/function call has no target.")
            quit()
