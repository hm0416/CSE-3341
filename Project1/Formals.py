from Id import Id
from Core import Core
import globals

class Formals:

    def parse(self, parser):
        self.id = Id()
        self.id.parse(parser)
        if parser.scanner.currentToken() == Core.COMMA:
            parser.scanner.nextToken()
            self.list = Formals()
            self.list.parse(parser)

    #gets all parameters that are passed into a function
    def getAllParams(self):
        params = [] #list of parameters
        if hasattr(self, 'list'): #if there is more than one paramater
            params = self.list.getAllParams()

        # if self.id.getString() in params:
        #     print("SEMANTIC ERROR: Function " + globals.funcDeclName + " formal parameters are not distinct from each other.")
        #     quit()
        # else:

        paramName = self.id.getString()
        params.append(paramName) #adds parameter to list

        return params