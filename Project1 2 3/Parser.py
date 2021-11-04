from Scanner import Scanner
import sys

# Parser class contains all the persistent data structures we will need, and some helper functions
class Parser:
	
	#Constructor for Parser.
	#scanner is stored here so it is avaiable to the parse method of all contained classes
	def __init__(self, s):
		self.scanner = Scanner(s)
	
	#helper method for handling error messages, used by the parse methods
	def expectedToken(self, expected):
		if self.scanner.currentToken() != expected:
			print("ERROR: Expected " + expected.name + ", recieved " + self.scanner.currentToken().name + "\n", end='')
			sys.exit()
