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

    def execute(self, executor):
        strings = None
        if hasattr(self, 'list'):
            strings = self.list.execute(executor)
        else:
            strings = []
        strings.insert(0, self.id.getString())
        return strings