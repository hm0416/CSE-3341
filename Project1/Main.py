from Scanner import Scanner
from Core import Core
import sys

def main():
    # Initialize the scanner with the input file
    S = Scanner(sys.argv[1])
    intialTokensList = S.tokenizer(sys.argv[1])

    # Print the token stream
    while (S.currentToken(intialTokensList) != Core.EOF and S.currentToken(intialTokensList) != Core.ERROR):
        # Print the current token, with any extra data needed
        if (S.currentToken(intialTokensList) != None):
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
        intialTokensList = S.nextToken(sys.argv[1], intialTokensList)


if __name__ == "__main__":
    main()
