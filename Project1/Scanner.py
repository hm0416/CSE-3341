import itertools

from Core import Core
import re

class Scanner:

    # Constructor should open the file and find the first token
    def __init__(self, filename):
        file = open(filename, "r")
        # file.close()

    # Goes through each line in the input file and tokenizes
    def tokenizer(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        tokens = []
        mergedTokenList = [] #all tokens in one list for the entire file

        for line in lines:
            lineSplit = re.findall(r"[\w']+|[.,!?;$:%_<~=()+*-]|[\s']+", line)  # taken from stack overflow - https://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
            list_cycle = itertools.cycle(lineSplit) #https://www.kite.com/python/answers/how-to-get-the-next-element-while-cycling-through-a-list-in-python
            next(list_cycle)
            for i, v in enumerate(lineSplit):
                nextEle = next(list_cycle)
                # special case - when string is <=
                if v == "<" and nextEle == "=":
                    lineSplit[i:i+2] = [''.join(lineSplit[i:i+2])] #if < is proceeded by = without a space/any other chars between them, then joins the two elements
                # special case - to figure out how many ASSIGN's and EQUAL's to output when there are multiple ='s
                if v == "=":
                    count = 1 #number of EQUAL signs
                    while nextEle == "=":
                        count = count + 1
                        nextEle = next(list_cycle)
                        if nextEle != "=":
                            break
                    if count > 1:
                        q = count // 2 #gets quotient
                        qTemp = 0
                        k = i
                        while qTemp < q:
                            lineSplit[k:k+2] = [''.join(lineSplit[k:k+2])]
                            k = k + 1
                            qTemp = qTemp + 1
                        break
                    else:
                        continue
                #if string starts with numbers then we want to split it
                if re.match('(\d+)', v):
                    #find v in list and replace it with the split string
                    # tempLineSplit = lineSplit.copy()
                    indexOfV = lineSplit.index(v)
                    vSplit = re.split('(\d+)', v)
                    # tempLineSplit.pop(indexOfV)
                    # for ele in vSplit:
                    #     tempLineSplit.insert(indexOfV, ele)

            tokens.append(lineSplit)

        tokens.pop(indexOfV)
        for ele in vSplit:
            tokens.insert(indexOfV, ele)
        #appends all tokens into one big list
        for tokenList in tokens:
            mergedTokenList += tokenList

        return mergedTokenList

    # nextToken should advance the scanner to the next token
    def nextToken(self, listOfToks):
        if len(listOfToks) == 0: #checks if list is empty
            exit()

        listOfToks.pop(0) #gets next token and modifies the list by removing the next token
        return listOfToks

    # currentToken should return the current token
    def currentToken(self, initialTokensList):
        #goes through each token and returns corresponding ENUM
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
            elif v == 'ref':
                return Core.REF
            elif v == 'eof':
                return Core.EOF
            elif v == 'error':
                return Core.ERROR
            elif v == '=':
                return Core.ASSIGN
            elif v == '==':
                return Core.EQUAL
            elif v == '<':
                return Core.LESS
            elif v == '<=':
                return Core.LESSEQUAL
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
        #checks if string is only alphabetical or alphanumerical
        if str.isalpha() or str.isalnum():
            return str
        else:
            return "Not alphabetical."

    # If the current token is CONST, return the numerical value of the constant
    # Otherwise, return value does not matter
    def getCONST(self, numStr):
        #checks that string is only numerical
        if numStr.isnumeric() or re.search("^[0-9]+[a-zA-Z]+?", numStr):
            return numStr
        else:
            return "Not a digit."
