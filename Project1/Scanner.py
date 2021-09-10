from Core import Core
import re


class Scanner:

    # Constructor should open the file and find the first token
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.file.close()

    # Goes through each line in the input file and tokenizes
    def tokenizer(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        tokens = []
        mergedTokenList = []  # all tokens in one list for the entire file

        for line in lines:
            if ' ' in line:
                lineSplit = re.findall(r"[\w']+|[@#&^`/{}|.,!?;$:%_><~=()+*-]|[\s']+",
                                       line)  # taken from stack overflow - https://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
            elif re.match('(\d+)', line):  # Special case - when a string starts with digits and ends with non-digits
                lineSplit = re.split('(\d+)', line)  # split the numbers and chars
                for ele in lineSplit:
                    if ele == '':
                        lineSplit.remove('')  # remove unecessary char
            else:
                lineSplit = re.findall(r"[\w']+|[@#&^`/{}|.,!?;$:%_><~=()+*-]|[\s']+",
                                       line)  # taken from stack overflow - https://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation

            tokens.append(lineSplit)

        # appends all tokens into one big list
        for tokenList in tokens:
            mergedTokenList += tokenList

        file.close()
        return mergedTokenList

    # nextToken should advance the scanner to the next token
    def nextToken(self, listOfToks):
        if len(listOfToks) == 0:  # checks if list is empty
            exit()

        listOfToks.pop(0)  # gets next token and modifies the list by removing the next token
        return listOfToks

    # currentToken should return the current token
    def currentToken(self, initialTokensList):
        # goes through each token and returns corresponding ENUM
        for i, v in enumerate(initialTokensList):
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
            elif v == 'or':
                return Core.OR
            elif v == 'ref':
                return Core.REF
            elif v == 'eof':
                return Core.EOF
            elif v == 'error':
                return Core.ERROR
            elif v == '<':
                #checks to see what the next char is after <
                if initialTokensList.index(v) != (len(initialTokensList) - 1):
                    nextChar = initialTokensList[i + 1]
                    if nextChar == "=":
                        initialTokensList[i:i + 2] = [''.join(initialTokensList[i:i + 2])] #joins < and = to make <=
                    else:
                        return Core.LESS
                else:
                    return Core.LESS
            elif v == "<=":
                return Core.LESSEQUAL
            elif v == '=':
                #checks to see what the next char is after =
                if initialTokensList.index(v) != (len(initialTokensList) - 1):
                    nextChar = initialTokensList[i + 1]
                    if nextChar == "=":
                        initialTokensList[i:i + 2] = [''.join(initialTokensList[i:i + 2])] #joins the two = symbols to make an EQUAL
                    else:
                        return Core.ASSIGN
                else:
                    return Core.ASSIGN
            elif v == '==':
                return Core.EQUAL
            elif v.isalpha():
                return Core.ID
            elif v.isnumeric():
                if int(v) > 1023:
                    print("Integers larger than 1023 are not allowed.\n")
                    quit()
                else:
                    return Core.CONST
            elif v.isspace():
                return ' '
            elif v.isalnum() and not v.isnumeric():
                return Core.ID
            else:
                print("Error " + v + " is not part of the language \n")
                quit()

    # If the current token is ID, return the string value of the identifier
    # Otherwise, return value does not matter
    def getID(self, str):
        # checks if string is only alphabetical or alphanumerical
        if str.isalpha() or str.isalnum():
            return str
        else:
            return "Not alphabetical."

    # If the current token is CONST, return the numerical value of the constant
    # Otherwise, return value does not matter
    def getCONST(self, numStr):
        # checks that string is only numerical
        if numStr.isnumeric():
            return numStr
        else:
            return "Not a digit."
