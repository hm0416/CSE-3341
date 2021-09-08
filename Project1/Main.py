from Scanner import Scanner
from Core import Core
import sys

# sys.argv[1]
# '/Users/hm0416/Desktop/CSE-3341/Project1/Correct/2.code'

def main():
    # Initialize the scanner with the input file
    S = Scanner('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/test')
    initialTokensList = S.tokenizer('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/test')

    # Print the token stream
    while (S.currentToken(initialTokensList) != Core.EOF and S.currentToken(initialTokensList) != Core.ERROR):
        # Print the current token, with any extra data needed
        if S.currentToken(initialTokensList) != None:
            if S.currentToken(initialTokensList) != ' ': #as long as token is not a space
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
        # Advance to the next token
        initialTokensList = S.nextToken(initialTokensList)


if __name__ == "__main__":
    main()
