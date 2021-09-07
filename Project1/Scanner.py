import itertools

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
            lineSplit = re.findall(r"[\w']+|[.,!?;<=()+*-]|[\s']+", line)  # taken from stack overflow - https://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
            # i = 0
            # while i <= len(lineSplit):
            #     temp = i
            #     if lineSplit[i] == "<" and lineSplit[temp + 1] == "=":
            #         lineSplit[i:temp+2] = [''.join(lineSplit[i:temp+2])]
            #     if lineSplit[i] == "=" and lineSplit[temp + 1] == "=":
            #         lineSplit[i:temp+2] = [''.join(lineSplit[i:temp+2])]
            #     i = i + 1
            list_cycle = itertools.cycle(lineSplit)
            next(list_cycle)
            for i, v in enumerate(lineSplit):
                nextEle = next(list_cycle)
                if v == "<" and nextEle == "=":
                    lineSplit[i:i+2] = [''.join(lineSplit[i:i+2])]
                if v == "=" and next(list_cycle) == "=":
                    lineSplit[i:i+2] = [''.join(lineSplit[i:i+2])]

            tokens.append(lineSplit)

        for tokenList in tokens:
            mergedTokenList += tokenList

        return mergedTokenList

    # nextToken should advance the scanner to the next token
    def nextToken(self, list):
        if len(list) == 0:
            exit()
        list.pop(0)
        return list  # need to modify the actual list

    # currentToken should return the current token
    def currentToken(self, intialTokensList):
        for i, v in enumerate(intialTokensList):
            if v == ';':
                return Core.SEMICOLON
            elif v == ',':
                return Core.COMMA
            elif v == '!':
                return Core.NEGATION
            elif v == '+':
                return Core.ADD
            elif v == '-':
                return Core.SUB
            elif v == '*':
                return Core.MULT
            elif v == '(':
                return Core.LPAREN
            elif v == ')':
                return Core.RPAREN
            elif v == 'begin':
                return Core.BEGIN
            elif v == 'program':
                return Core.PROGRAM
            elif v == 'end':
                return Core.END
            elif v == 'new':
                return Core.NEW
            elif v == 'define':
                return Core.DEFINE
            elif v == 'extends':
                return Core.EXTENDS
            elif v == 'class':
                return Core.CLASS
            elif v == 'endclass':
                return Core.ENDCLASS
            elif v == 'int':
                return Core.INT
            elif v == 'endfunc':
                return Core.ENDFUNC
            elif v == 'if':
                return Core.IF
            elif v == 'then':
                return Core.THEN
            elif v == 'else':
                return Core.ELSE
            elif v == 'while':
                return Core.WHILE
            elif v == 'endwhile':
                return Core.ENDWHILE
            elif v == 'endif':
                return Core.ENDIF
            elif v == 'input':
                return Core.INPUT
            elif v == 'output':
                return Core.OUTPUT
            elif v == 'ref':
                return Core.REF
            elif v == 'eof':
                return Core.EOF
            elif v == 'error':
                return Core.ERROR
            elif v == '=':
                # if i < len(intialTokensList) and intialTokensList[i + 1] == "=":
                #     i = i + 1
                #     return Core.EQUAL
                # else:
                return Core.ASSIGN
            elif v == '==':
                return Core.EQUAL
            elif v == '<':
                # if i < len(intialTokensList) and intialTokensList[i + 1] == "=":
                #     i = i + 1
                #     return Core.LESSEQUAL
                # else:
                return Core.LESS
            elif v == '<=':
                return Core.LESSEQUAL
            elif v.isalpha():
                return Core.ID
            elif v.isnumeric():
                if int(v) > 1023:
                    print("Integers larger than 1023 are not allowed.")
                else:
                    return Core.CONST

    # If the current token is ID, return the string value of the identifier
    # Otherwise, return value does not matter
    def getID(self, str):
        if str.isalpha() or str.isalnum():
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
