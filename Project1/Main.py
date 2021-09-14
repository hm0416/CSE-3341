from Scanner import Scanner
from Core import Core
import sys


def main():
    # Initialize the scanner with the input file
    S = Scanner(sys.argv[1])
    initialTokensList = S.tokenizer(sys.argv[1]) #tokenizes the input file and returns a list of tokens for specified file

    # Print the token stream
    while (S.currentToken(initialTokensList) != Core.EOF and S.currentToken(initialTokensList) != Core.ERROR):
        # Print the current token, with any extra data needed
        if S.currentToken(initialTokensList) != None:
            if S.currentToken(initialTokensList) != ' ':  # as long as token is not a space
                print(S.currentToken(initialTokensList).name, end='')

            if S.currentToken(initialTokensList) == Core.ID:
                currentStr = initialTokensList[0]
                value = S.getID(currentStr)
                print("[" + value + "]", end='')
            elif S.currentToken(initialTokensList) == Core.CONST:
                numStr = initialTokensList[0]
                value = S.getCONST(numStr)
                print("[" + str(value) + "]", end='')
        if S.currentToken(initialTokensList) != ' ':
            print()

        if len(initialTokensList) == 1: #if initialTokenList has len of one that means we've reached the last char/string so set to EOF after printing that last char/string
            S.currentToken(initialTokensList) == Core.EOF

        # Advance to the next token
        initialTokensList = S.nextToken(initialTokensList)




if __name__ == "__main__":
    main()
