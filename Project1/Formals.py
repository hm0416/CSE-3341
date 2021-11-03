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

    def print(self):
        self.id.print()
        if hasattr(self, 'list'):
            print(",", end='')
            self.list.print()

    def getAllParams(self, executor):
        params = [] #list of parameters
        if hasattr(self, 'list'): #if there is more than one paramater
            params = self.list.getAllParams(executor)
        params.append(self.id.getString()) #adds parameter to list

        return params