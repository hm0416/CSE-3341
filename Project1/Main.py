from Scanner import Scanner
from Core import Core
import sys

def main():
    # S = Scanner('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/1.code')
    #
    # file = open('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/1.code', "r")
    # lines = file.readlines()
    # tokens = []
    # mergedTokenList = []
    # for line in lines:
    #     tokens.append(line.split())
    #
    # for tokenList in tokens:
    #     mergedTokenList += tokenList
    # #
    # for i, v in enumerate(mergedTokenList):
    #     if ';' in v:
    #         mergedTokenList[i] = v.replace(';', 'SEMICOLON')
    #     elif ',' in v:
    #         mergedTokenList[i] = v.replace(',', 'COMMA')
    #     elif '!' in v:
    #         mergedTokenList[i] = v.replace('!', 'NEGATION')
    #     elif '+' in v:
    #         mergedTokenList[i] = v.replace('+', 'ADD')
    #     elif '-' in v:
    #         mergedTokenList[i] = v.replace('-', 'SUB')
    #     elif '*' in v:
    #         mergedTokenList[i] = v.replace('*', 'MULT')
    #     elif '(' in v:
    #         mergedTokenList[i] = v.replace('(', 'LPAREN')
    #     elif ')' in v:
    #         mergedTokenList[i] = v.replace(')', 'RPAREN')
    #     elif 'begin' in v:
    #         mergedTokenList[i] = v.replace('begin', 'BEGIN')
    #     elif 'program' in v:
    #         mergedTokenList[i] = v.replace('program', 'PROGRAM')
    #     elif 'end' in v:
    #         mergedTokenList[i] = v.replace('end', 'END')
    #     elif 'new' in v:
    #         mergedTokenList[i] = v.replace('new', 'NEW')
    #     elif 'define' in v:
    #         mergedTokenList[i] = v.replace('define', 'DEFINE')
    #     elif 'extends' in v:
    #         mergedTokenList[i] = v.replace('extends', 'EXTENDS')
    #     elif 'class' in v:
    #         mergedTokenList[i] = v.replace('class', 'CLASS')
    #     elif 'endclass' in v:
    #         mergedTokenList[i] = v.replace('endclass', 'ENDCLASS')
    #     elif 'int' in v:
    #         mergedTokenList[i] = v.replace('int', 'INT')
    #     elif 'endfunc' in v:
    #         mergedTokenList[i] = v.replace('endfunc', 'ENDFUNC')
    #     elif 'if' in v:
    #         mergedTokenList[i] = v.replace('if', 'IF')
    #     elif 'then' in v:
    #         mergedTokenList[i] = v.replace('then', 'THEN')
    #     elif 'else' in v:
    #         mergedTokenList[i] = v.replace('else', 'ELSE')
    #     elif 'while' in v:
    #         mergedTokenList[i] = v.replace('while', 'WHILE')
    #     elif 'endwhile' in v:
    #         mergedTokenList[i] = v.replace('endwhile', 'ENDWHILE')
    #     elif 'endif' in v:
    #         mergedTokenList[i] = v.replace('endif', 'ENDIF')
    #     elif 'input' in v:
    #         mergedTokenList[i] = v.replace('input', 'INPUT')
    #     elif 'output' in v:
    #         mergedTokenList[i] = v.replace('output', 'OUTPUT')
    #     elif 'ref' in v:
    #         mergedTokenList[i] = v.replace('ref', 'REF')
    #     elif 'eof' in v:
    #         mergedTokenList[i] = v.replace('eof', 'EOF')
    #     elif 'error' in v:
    #         mergedTokenList[i] = v.replace('error', 'ERROR')
    #     elif '==' in v:
    #       mergedTokenList[i] = v.replace('==', 'EQUAL')
    #     elif '=' in v:
    #       mergedTokenList[i] = v.replace('=', 'ASSIGN')
    #     elif '<' in v:
    #       mergedTokenList[i] = v.replace('<', 'LESS')
    #     elif '<=' in v:
    #       mergedTokenList[i] = v.replace('<=', 'LESSEQUAL')
    #     elif v.isalpha():
    #       mergedTokenList[i] = v.replace(v, 'ID[' + v + "]")
    #     elif v.isnumeric():
    #       mergedTokenList[i] = v.replace(v, 'CONST[' + v + "]")

    #
    # tok = S.nextToken('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/1.code')
    #
    # print(mergedTokenList)

    # tempMergedTokenList = mergedTokenlist.copy()

    # nextTok = tempMergedTokenList[0]

    # Initialize the scanner with the input file
    S = Scanner('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/1.code')
    intialTokensList = S.tokenizer('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/1.code')
    # firstTok = intialTokensList[0]
    # S.nextToken('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/1.code', intialTokensList)

    # Print the token stream
    while (S.currentToken(intialTokensList) != Core.EOF and S.currentToken(intialTokensList) != Core.ERROR):
        # Print the current token, with any extra data needed
        print(S.currentToken(intialTokensList).name, end='')
        if (S.currentToken(intialTokensList) == Core.ID):
            currentStr = intialTokensList[0]
            value = S.getID(currentStr)
            print("[" + value + "]", end='')
        elif (S.currentToken(intialTokensList) == Core.CONST):
            numStr = intialTokensList[0]
            value = S.getCONST(numStr)
            print("[" + str(value) + "]", end='')
        print()
        # Advance to the next token
        intialTokensList = S.nextToken('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/1.code', intialTokensList)


if __name__ == "__main__":
    main()

# sys.argv[1]