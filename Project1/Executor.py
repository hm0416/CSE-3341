from Scanner import Scanner
from Core import Core
import sys

class CoreVar:
    def __init__(self, varType):
        self.type = varType
        self.value = None
        if self.type == Core.INT:
            self.value = 0

class Executor:

    def __init__(self, s):
        self.globalSpace = {}
        self.heapSpace = []
        self.dataFile = Scanner(s)
        
        self.stackSpace = []
        self.funcDefinitions = {}
        self.refCounts = [] #list of ints - keeps track of reference counts
        self.counter = 0

    def pushLocalScope(self):
        self.stackSpace[-1].append({})
	
    def popLocalScope(self):
        self.stackSpace[-1].pop()
        self.counter = self.counter + 1  # increment the number of references because a variable has been declared as "new"

    def getNextData(self):
        data = 0
        if self.dataFile.currentToken() == Core.EOF:
            print("ERROR: data file is out of values!\n", end='')
            sys.exit()
        else:
            data = self.dataFile.getCONST()
            self.dataFile.nextToken()
        return data
	
    def allocate(self, identifier, varType):
        record = CoreVar(varType)
        # If we are in the DeclSeq, the local scope will not be created yet
        if len(self.stackSpace)==0:
            self.globalSpace[identifier] = record
        else:
            self.stackSpace[-1][-1][identifier] = record
	
    def getStackOrStatic(self, identifier):
        record = None
        for x in reversed(self.stackSpace[-1]):
            if identifier in x:
                record = x[identifier]
                break
        if record == None:
            record = self.globalSpace[identifier]
        return record
	
    def heapAllocate(self, identifier):
        x = self.getStackOrStatic(identifier)
        if x.type != Core.REF:
            print("ERROR: " + identifier + " is not of type ref, cannot perform \"new\:-assign!\n", end='')
            sys.exit()
        x.value = len(self.heapSpace)
        self.heapSpace.append(None)
        self.refCounts.append(None) #heap grew, so ref counts grows too
	
    def getType(self, identifier):
        x = self.getStackOrStatic(identifier)
        return x.type
	
    def getValue(self, identifier):
        x = self.getStackOrStatic(identifier)
        value = x.value
        if x.type == Core.REF:
            try:
                value = self.heapSpace[value]
            except IndexError:
                print("ERROR: invalid heap read attempted!\n", end='')
                sys.exit()
            except TypeError:
                print("ERROR: invalid heap read attempted!\n", end='')
                sys.exit()
        return value
	
    def storeValue(self, identifier, value):
        x = self.getStackOrStatic(identifier)
        if x.type == Core.REF:
            try:
                self.heapSpace[x.value] = value
            except IndexError:
                print("ERROR: invalid heap write attempted!\n", end='')
                sys.exit()
            except TypeError:
                print("ERROR: invalid heap write attempted!\n", end='')
                sys.exit()
        else:
            x.value = value

    def referenceCopy(self, var1, var2):
        x = self.getStackOrStatic(var1)
        y = self.getStackOrStatic(var2)
        x.value = y.value




    # New methods to handle pushing/popping frames and storing fucntion definitions

    def storeFuncDef(self, name, definition):
        self.funcDefinitions[name.getString()] = definition

    def getFormalParams(self, name):
        if name.getString() not in self.funcDefinitions:
            print("ERROR: Function call " + name.getString() + " has no target!" + "\n", end='')
            sys.exit()
        return self.funcDefinitions[name.getString()].getFormalParams()

    def getBody(self, name):
        return self.funcDefinitions[name.getString()].getBody()

    def pushMainFrame(self):
        self.stackSpace.append([])
        self.pushLocalScope()

    def pushFrame(self, formalParams, actualParams):
        formals = formalParams.execute(self)
        actuals = actualParams.execute(self)

        newFrame = []
        newFrame.append({})

        for i in range(len(formals)):
            temp = CoreVar(Core.REF)
            temp.value = self.getStackOrStatic(actuals[i]).value
            newFrame[-1][formals[i]] = temp

        self.stackSpace.append(newFrame)
        self.pushLocalScope()

    def popFrame(self):
        self.stackSpace.pop()
        self.counter = self.counter - 1  # increment the number of references because a variable has been declared as "new"
