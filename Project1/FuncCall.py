from Core import Core
from Executor import CoreVar
from Formals import Formals
from Id import Id
import globals


class FuncCall:
    def parse(self, parser):
        # parser.expectedToken(Core.BEGIN)
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

    # def execute(self, executor):
    #     formalParams = executor.getFormalParams(self.id)
    #     body = executor.getBody(self.id)
    #
    #     formals = formalParams.execute(self)
    #     actuals = self.actualParams.execute(self)
    #
    #     newFrame = []
    #     newFrame.append({})
    #
    #     for i in range(len(formals)):
    #         temp = CoreVar(Core.CLASS)
    #         temp.value = executor.getStackOrStatic(actuals[i]).value
    #         newFrame[-1][formals[i]] = temp
    #
    #     executor.stackSpace.append(newFrame)
    #     executor.pushLocalScope()
    #     body.execute(executor)
    #     executor.stackSpace.pop()

    def execute(self, executor):

        #get all the formal params
        #get body of the function
        #get all the actual params

        #for each formal param, find the corresponding actual param on the stack or static and get its value

        formalParams = globals.formals.execute(self) #gets all formals by calling execute
        actualParams = self.actualParams.execute(self)
        stackFrame = {}
        for i in range(len(formalParams)):
            heapIndex = CoreVar(Core.REF)
            heapIndex.value = executor.getStackOrStatic(actualParams[i]).value
            stackFrame[formalParams[i]] = heapIndex
            # executor.heapSpace[0] = 10
            # executor.heapSpace[1] = 10

        executor.stackSpace.append(stackFrame)
        # executor.pushLocalScope()
        globals.bod.execute(executor)





        # globals.isFunc = True
        # globals.bod.execute(executor)



        # formalParams = executor.getFormalParams(self.id)
        # fp = formalParams.execute(self)
        # body = executor.getBody(self.id)


        # actualParams = self.actualParams.execute(self)
        # # valOfFormalParam = executor.getStackOrStatic(formalParams[0]).value
        # stackFrame = []
        # stackFrame.append({})

        # for i in range(len(formalParams)):
        # #     # executor.referenceCopy(actualParams[i], formalParams[i])
        # #     valOfActualParam = executor.getStackOrStatic(actualParams[i]).value #gets index into heap
        # #     executor.storeValue(actualParams[i], valOfActualParam)
        #     t = CoreVar(Core.REF)
        #     t.value = executor.getStackOrStatic(actualParams[i]).value
        #     stackFrame[-1][formalParams[i]] = t
        #
        # executor.stackSpace.append(stackFrame)
        # executor.pushLocalScope()
        #
        # globals.bod.execute(executor)
        # executor.stackSpace.pop()





        # formalParams = globals.formals.execute(self) #gets all formals by calling execute
        # body = globals.bod.execute(self)
        # formalParams = executor.getFormalParams(self.id)
        # fp = formalParams.execute(self)
        # body = executor.getBody(self.id)
        # actualParams = self.actualParams.execute(self)
        #
        # newFrame = []
        # newFrame.append({})
        #
        # for i in range(len(fp)):
        #     temp = CoreVar(Core.REF)
        #     temp.value = executor.getStackOrStatic(actualParams[i]).value
        #     newFrame[-1][fp[i]] = temp
        #
        # executor.stackSpace.append(newFrame)
        # executor.pushLocalScope()
        #
        # body.execute(executor)
        # print(body)
        # executor.stackSpace.pop()
