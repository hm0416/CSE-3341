from Id import Id
from Core import Core

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
        paramName = self.id.getString() #gets the name of the parameter
        params.append(paramName) #adds parameter to list

        return params