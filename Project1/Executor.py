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
        self.stackSpace = []
        self.heapSpace = []
        self.dataFile = Scanner(s)
        self.func = {} #for function definitions
        self.stackFrame = {}  # stack for parameters

    def pushLocalScope(self):
        self.stackSpace.append({})
	
    def popLocalScope(self):
        self.stackSpace.pop()
	
    # Handles geting values for input statements
    def getNextData(self):
        data = 0
        if self.dataFile.currentToken() == Core.EOF:
            print("ERROR: data file is out of values!\n", end='')
            sys.exit()
        else:
            data = self.dataFile.getCONST()
            self.dataFile.nextToken()
        return data
	
    # Handles variable declarations
    def allocate(self, identifier, varType):
        record = CoreVar(varType)
        # If we are in the DeclSeq, the local scope will not be created yet
        if len(self.stackSpace)==0:
            self.globalSpace[identifier] = record
        else:
            self.stackSpace[-1][identifier] = record
	
    # Finds out where a variable is stored
    def getStackOrStatic(self, identifier):
        record = None
        for x in reversed(self.stackSpace):
            if identifier in x:
                record = x[identifier]
                break
        if record == None:
            record = self.globalSpace[identifier]
        return record
	
    # Handles "new" assignments
    def heapAllocate(self, identifier):
        x = self.getStackOrStatic(identifier)
        if x.type != Core.REF:
            print("ERROR: " + identifier + " is not of type ref, cannot perform \"new\:-assign!\n", end='')
            sys.exit()
        x.value = len(self.heapSpace)
        self.heapSpace.append(None)
	
    # Returns the declared type of a variable
    def getType(self, identifier):
        x = self.getStackOrStatic(identifier)
        return x.type
	
    # Gets the r-value of a variable
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
	
    # Used to store values to int and ref variables
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

    # Handles "ref"-type assignments
    def referenceCopy(self, var1, var2):
        x = self.getStackOrStatic(var1)
        y = self.getStackOrStatic(var2)
        x.value = y.value
