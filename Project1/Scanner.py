from Core import Core

class Scanner:
  # Constructor should open the file and find the first token
  def __init__(self, filename):
    file = open(filename, "r")
    self.nextToken()

  #tokenzies everything, then we need to go through each element in the mergedTokenList and replace its value with what
  #it's supposed to be based on ENUM
  def tokenizer(self, filename):
    file = open(filename, "r")
    lines = file.readlines()
    tokens = []
    mergedTokenList = []
    for line in lines:
      tokens.append(line.split())

    for tokenList in tokens:
      mergedTokenList += tokenList

    # return mergedTokenlist[index + 1]
    # tempMergedTokenList = mergedTokenlist.copy()
    # return tempMergedTokenList.pop(0)

    for i, v in enumerate(mergedTokenList):
      if ';' in v:
        mergedTokenList[i] = v.replace(';', 'SEMICOLON')
      elif ',' in v:
        mergedTokenList[i] = v.replace(',', 'COMMA')
      elif '!' in v:
        mergedTokenList[i] = v.replace('!', 'NEGATION')
      elif '+' in v:
        mergedTokenList[i] = v.replace('+', 'ADD')
      elif  '-' in v:
        mergedTokenList[i] = v.replace('-', 'SUB')
      elif '*' in v:
        mergedTokenList[i] = v.replace('*', 'MULT')
      elif '(' in v:
        mergedTokenList[i] = v.replace('(', 'LPAREN')
      elif  ')' in v:
        mergedTokenList[i] = v.replace(')', 'RPAREN')
      elif 'begin' in v:
        mergedTokenList[i] = v.replace('begin', 'BEGIN')
      elif 'program' in v:
        mergedTokenList[i] = v.replace('program', 'PROGRAM')
      elif 'end' in v:
        mergedTokenList[i] = v.replace('end', 'END')
      elif 'new' in v:
        mergedTokenList[i] = v.replace('new', 'NEW')
      elif 'define' in v:
        mergedTokenList[i] = v.replace('define', 'DEFINE')
      elif 'extends' in v:
        mergedTokenList[i] = v.replace('extends', 'EXTENDS')
      elif 'class' in v:
        mergedTokenList[i] = v.replace('class', 'CLASS')
      elif 'endclass' in v:
        mergedTokenList[i] = v.replace('endclass', 'ENDCLASS')
      elif 'int' in v:
        mergedTokenList[i] = v.replace('int', 'INT')
      elif 'endfunc' in v:
        mergedTokenList[i] = v.replace('endfunc', 'ENDFUNC')
      elif 'if' in v:
        mergedTokenList[i] = v.replace('if', 'IF')
      elif 'then' in v:
        mergedTokenList[i] = v.replace('then', 'THEN')
      elif 'else' in v:
        mergedTokenList[i] = v.replace('else', 'ELSE')
      elif 'while' in v:
        mergedTokenList[i] = v.replace('while', 'WHILE')
      elif 'endwhile' in v:
        mergedTokenList[i] = v.replace('endwhile', 'ENDWHILE')
      elif 'endif' in v:
        mergedTokenList[i] = v.replace('endif', 'ENDIF')
      elif 'input' in v:
        mergedTokenList[i] = v.replace('input', 'INPUT')
      elif 'output' in v:
        mergedTokenList[i] = v.replace('output', 'OUTPUT')
      elif 'ref' in v:
        mergedTokenList[i] = v.replace('ref', 'REF')
      elif 'eof' in v:
        mergedTokenList[i] = v.replace('eof', 'EOF')
      elif 'error' in v:
        mergedTokenList[i] = v.replace('error', 'ERROR')
      elif  '=' in v:
        nextChar = self.nextToken(filename)
        if nextChar == '=':
          # read char before return
          mergedTokenList[i] = v.replace('==', 'EQUAL')
        else:
          mergedTokenList[i] = v.replace('=', 'ASSIGN')
      elif '<' in v:
        nextChar = self.nextToken(filename)
        if nextChar == '=':
          # read char before return
          mergedTokenList[i] = v.replace('<=', 'LESSEQUAL')
        else:
          mergedTokenList[i] = v.replace('<', 'LESS')
      # elif mergedTokenList[i].isalpha():
      #   while(self.nextToken()):
      #
      # elif mergedTokenList[i].isnumeric():
      #   while (self.nextToken()):


  # nextToken should advance the scanner to the next token
  # def nextToken(self, filename):

  # currentToken should return the current token
  # def currentToken(self, filename):
    # currentTok = self.nextToken(filename)

    # if currentTok == ';':
    #   return Core.SEMICOLON
    # elif currentTok == ',':
    #   return Core.COMMA
    # elif currentTok == '!':
    #   return Core.NEGATION
    # elif currentTok == '+':
    #   return Core.ADD
    # elif currentTok == '-':
    #   return Core.SUB
    # elif currentTok == '*':
    #   return Core.MULT
    # elif currentTok == '(':
    #   return Core.LPAREN
    # elif currentTok == ')':
    #   return Core.RPAREN
    # elif currentTok == '=':
    #   nextChar = self.nextToken(filename)
    #   if nextChar == '=':
    #     #read char before return
    #     return Core.EQUAL
    #   else:
    #     return Core.ASSIGN
    # elif currentTok == '<':
    #   nextChar = self.nextToken(filename)
    #   if nextChar == '=':
    #     #read char before return
    #     return Core.LESSEQUAL
    #   else:
    #     return Core.LESS
    # # elif currentChar.isalpha():
    # #   while(self.nextToken()):
    # #     if
    # #
    # # elif currentChar.isnumeric():
    # #   while (self.nextToken()):


  # If the current token is ID, return the string value of the identifier
	# Otherwise, return value does not matter
  def getID(self):
    return ""

  # If the current token is CONST, return the numerical value of the constant
	# Otherwise, return value does not matter
  def getCONST(self):
    return 0