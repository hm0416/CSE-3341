from Scanner import Scanner
from Core import Core
import sys

# sys.argv[1]
# '/Users/hm0416/Desktop/CSE-3341/Project1/Correct/2.code'

def main():
    # Initialize the scanner with the input file
    S = Scanner('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/11.code')
    intialTokensList = S.tokenizer('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/11.code')

    # Print the token stream
    while (S.currentToken(intialTokensList) != Core.EOF and S.currentToken(intialTokensList) != Core.ERROR):
        # Print the current token, with any extra data needed
        if S.currentToken(intialTokensList) != None:
            if S.currentToken(intialTokensList) != ' ':
                print(S.currentToken(intialTokensList).name, end='')
            if S.currentToken(intialTokensList) == Core.ID:
                currentStr = intialTokensList[0]
                value = S.getID(currentStr)
                print("[" + value + "]", end='')
            elif S.currentToken(intialTokensList) == Core.CONST:
                numStr = intialTokensList[0]
                value = S.getCONST(numStr)
                print("[" + str(value) + "]", end='')
        if S.currentToken(intialTokensList) != ' ':
            print()
        # Advance to the next token
        intialTokensList = S.nextToken(intialTokensList)


if __name__ == "__main__":
    main()
