from Core import Core

class Scanner:

  # Constructor should open the file and find the first token
  def __init__(self, filename):
    file = open(filename, "r")
    # self.nextToken(filename, )

  #tokenzies everything, then we need to go through each element in the mergedTokenList and replace its value with what
  #it's supposed to be based on ENUM
  def tokenizer(self, filename):
    file = open(filename, "r")
    lines = file.readlines()
    tokens = []
    mergedTokenList = []
    # global tempMergedTokenList

    for line in lines:
      tokens.append(line.split())

    for tokenList in tokens:
      mergedTokenList += tokenList

    # tempMergedTokenList = mergedTokenList.copy()
    #
    # # return mergedTokenlist[index + 1]
    # # tempMergedTokenList = mergedTokenList.copy()
    # # return tempMergedTokenList.pop(0)
    #
    return mergedTokenList


  # nextToken should advance the scanner to the next token
  def nextToken(self, filename, list):
    list.pop(0)
    return list #need to modify the actual list


  # currentToken should return the current token
  def currentToken(self, intialTokensList):
    for i, v in enumerate(intialTokensList):
      if ';' in v:
        return Core.SEMICOLON
      elif ',' in v:
        return Core.COMMA
      elif '!' in v:
        return Core.NEGATION
      elif '+' in v:
        return Core.ADD
      elif '-' in v:
        return Core.SUB
      elif '*' in v:
        return Core.MULT
      elif '(' in v:
        return Core.LPAREN
      elif ')' in v:
        return Core.RPAREN
      elif 'begin' in v:
        return Core.BEGIN
      elif 'program' in v:
        return Core.PROGRAM
      elif 'end' in v:
        return Core.END
      elif 'new' in v:
        return Core.NEW
      elif 'define' in v:
        return Core.DEFINE
      elif 'extends' in v:
        return Core.EXTENDS
      elif 'class' in v:
        return Core.CLASS
      elif 'endclass' in v:
        return Core.ENDCLASS
      elif 'int' in v:
        return Core.INT
      elif 'endfunc' in v:
        return Core.ENDFUNC
      elif 'if' in v:
        return Core.IF
      elif 'then' in v:
        return Core.THEN
      elif 'else' in v:
        return Core.ELSE
      elif 'while' in v:
        return Core.WHILE
      elif 'endwhile' in v:
        return Core.ENDWHILE
      elif 'endif' in v:
        return Core.ENDIF
      elif 'input' in v:
        return Core.INPUT
      elif 'output' in v:
        return Core.OUTPUT
      elif 'ref' in v:
        return Core.REF
      elif 'eof' in v:
        return Core.EOF
      elif 'error' in v:
        return Core.ERROR
      elif '==' in v:
        return Core.EQUAL
      elif '=' in v:
        return Core.ASSIGN
      elif '<' in v:
        return Core.LESS
      elif '<=' in v:
        return Core.LESSEQUAL
      elif v.isalpha():
        return Core.ID
      elif v.isnumeric():
        return Core.CONST

  # If the current token is ID, return the string value of the identifier
	# Otherwise, return value does not matter
  def getID(self, str):
    if str.isalpha():
      return str
    else:
      return "not alpha"

  # If the current token is CONST, return the numerical value of the constant
	# Otherwise, return value does not matter
  def getCONST(self, numStr):
    if numStr.isnumeric():
      return numStr
    else:
      return "not digit"


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


    # for i, v in enumerate(mergedTokenList):
    #   if ';' in v:
    #     mergedTokenList[i] = v.replace(';', Core.SEMICOLON)
    #   elif ',' in v:
    #     mergedTokenList[i] = v.replace(',', Core.COMMA)
    #   elif '!' in v:
    #     mergedTokenList[i] = v.replace('!', Core.NEGATION)
    #   elif '+' in v:
    #     mergedTokenList[i] = v.replace('+', Core.ADD)
    #   elif '-' in v:
    #     mergedTokenList[i] = v.replace('-', Core.SUB)
    #   elif '*' in v:
    #     mergedTokenList[i] = v.replace('*', Core.MULT)
    #   elif '(' in v:
    #     mergedTokenList[i] = v.replace('(', Core.LPAREN)
    #   elif ')' in v:
    #     mergedTokenList[i] = v.replace(')', Core.RPAREN)
    #   elif 'begin' in v:
    #     mergedTokenList[i] = v.replace('begin', Core.BEGIN)
    #   elif 'program' in v:
    #     mergedTokenList[i] = Core.PROGRAM
    #   elif 'end' in v:
    #     mergedTokenList[i] = v.replace('end', Core.END)
    #   elif 'new' in v:
    #     mergedTokenList[i] = v.replace('new', Core.NEW)
    #   elif 'define' in v:
    #     mergedTokenList[i] = v.replace('define', Core.DEFINE)
    #   elif 'extends' in v:
    #     mergedTokenList[i] = v.replace('extends', Core.EXTENDS)
    #   elif 'class' in v:
    #     mergedTokenList[i] = v.replace('class', Core.CLASS)
    #   elif 'endclass' in v:
    #     mergedTokenList[i] = v.replace('endclass', Core.ENDCLASS)
    #   elif 'int' in v:
    #     mergedTokenList[i] = v.replace('int', Core.INT)
    #   elif 'endfunc' in v:
    #     mergedTokenList[i] = v.replace('endfunc', Core.ENDFUNC)
    #   elif 'if' in v:
    #     mergedTokenList[i] = v.replace('if', Core.IF)
    #   elif 'then' in v:
    #     mergedTokenList[i] = v.replace('then', Core.THEN)
    #   elif 'else' in v:
    #     mergedTokenList[i] = v.replace('else', Core.ELSE)
    #   elif 'while' in v:
    #     mergedTokenList[i] = v.replace('while', Core.WHILE)
    #   elif 'endwhile' in v:
    #     mergedTokenList[i] = v.replace('endwhile', Core.ENDWHILE)
    #   elif 'endif' in v:
    #     mergedTokenList[i] = v.replace('endif', Core.ENDIF)
    #   elif 'input' in v:
    #     mergedTokenList[i] = v.replace('input', Core.INPUT)
    #   elif 'output' in v:
    #     mergedTokenList[i] = v.replace('output', Core.OUTPUT)
    #   elif 'ref' in v:
    #     mergedTokenList[i] = v.replace('ref', Core.REF)
    #   elif 'eof' in v:
    #     mergedTokenList[i] = v.replace('eof', Core.EOF)
    #   elif 'error' in v:
    #     mergedTokenList[i] = v.replace('error', Core.ERROR)
    #   elif '==' in v:
    #     mergedTokenList[i] = v.replace('==', Core.EQUAL)
    #   elif '=' in v:
    #     mergedTokenList[i] = v.replace('=', Core.ASSIGN)
    #   elif '<' in v:
    #     mergedTokenList[i] = v.replace('<', Core.LESS)
    #   elif '<=' in v:
    #     mergedTokenList[i] = v.replace('<=', Core.LESSEQUAL)
    #   elif v.isalpha():
    #     mergedTokenList[i] = v.replace(v, Core.ID + "[" + v + "]")
    #   elif v.isnumeric():
    #     mergedTokenList[i] = v.replace(v, Core.CONST + "[" + v + "]")