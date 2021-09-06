from Core import Core
import re

class Scanner:

    # Constructor should open the file and find the first token
    def __init__(self, filename):
        file = open(filename, "r")

    # tokenzies everything, then we need to go through each element in the mergedTokenList and replace its value with what
    # it's supposed to be based on ENUM
    def tokenizer(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        tokens = []
        mergedTokenList = []

        for line in lines:
            lineSplit = re.findall(r"[\w']+|[.,!?;=()<+*-]", line)  # taken from stack overflow - https://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
            tokens.append(lineSplit)

        for tokenList in tokens:
            mergedTokenList += tokenList

        return mergedTokenList

    # nextToken should advance the scanner to the next token
    def nextToken(self, filename, list):
        if len(list) == 0:
            exit()
        list.pop(0)
        return list  # need to modify the actual list

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
