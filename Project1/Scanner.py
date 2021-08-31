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
  def currentToken(self, filename):
    file = open(filename, "r")
    currentChar = file.read()

    if currentChar == ';':
      return Core.SEMICOLON
    elif currentChar == ',':
      return Core.COMMA
    elif currentChar == '!':
      return Core.NEGATION
    elif currentChar == '+':
      return Core.ADD
    elif currentChar == '-':
      return Core.SUB
    elif currentChar == '*':
      return Core.MULT
    elif currentChar == '(':
      return Core.LPAREN
    elif currentChar == ')':
      return Core.RPAREN
    elif currentChar == '=':
      nextChar = self.nextToken()
      if nextChar == '=':
        #read char before return
        return Core.EQUAL
      else:
        return Core.ASSIGN
    elif currentChar == '<':
      nextChar = self.nextToken()
      if nextChar == '=':
        #read char before return
        return Core.LESSEQUAL
      else:
        return Core.LESS
    elif currentChar.isalpha():
      while(self.nextToken()):
        if


    elif currentChar.isnumeric():
      while (self.nextToken()):


  # If the current token is ID, return the string value of the identifier
	# Otherwise, return value does not matter
  def getID(self):
    return ""

  # If the current token is CONST, return the numerical value of the constant
	# Otherwise, return value does not matter
  def getCONST(self):
    return 0