from Scanner import Scanner
from Core import Core
import sys

def main():
  file = open('/Users/hm0416/Desktop/CSE-3341/Project1/Correct/1.code', "r")
  lines = file.readlines()
  tokens = []
  mergedTokenList = []
  for line in lines:
    tokens.append(line.split())

  for tokenList in tokens:
    mergedTokenList += tokenList

  for i, v in enumerate(mergedTokenList):
    if ';' in v:
      mergedTokenList[i] = v.replace(';', 'SEMICOLON')

  print(mergedTokenList)




  # tempMergedTokenList = mergedTokenlist.copy()

  # nextTok = tempMergedTokenList[0]

  # Initialize the scanner with the input file
  S = Scanner(sys.argv[1])

  # Print the token stream
  while (S.currentToken() != Core.EOF and S.currentToken() != Core.ERROR):
    # Print the current token, with any extra data needed
    print(S.currentToken().name, end='')
    if (S.currentToken() == Core.ID):
      value = S.getID()
      print("[" + value + "]", end='')
    elif (S.currentToken() == Core.CONST):
      value = S.getCONST()
      print("[" + str(value) + "]", end='')
    print()
    # Advance to the next token
    S.nextToken()


if __name__ == "__main__":
    main()