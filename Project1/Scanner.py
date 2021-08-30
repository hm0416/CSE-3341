from Core import Core

class Scanner:
  # Constructor should open the file and find the first token
  def __init__(self, filename):
    file = open(filename, "r")
    self.currentToken()

  # nextToken should advance the scanner to the next token
  def nextToken(self):
    return 0

  # currentToken should return the current token
  def currentToken(self):
    return 0

  # If the current token is ID, return the string value of the identifier
	# Otherwise, return value does not matter
  def getID(self):
    return ""

  # If the current token is CONST, return the numerical value of the constant
	# Otherwise, return value does not matter
  def getCONST(self):
    return 0