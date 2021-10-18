from Parser import Parser
from Program import Program
from Scanner import Scanner
from Core import Core
import globals

import sys

def main():
  #Initialize globals file so can pass around variables throughout classes
  globals.initialize()
  # Initialize the parser object (contains the scanner and some helper functions)
  parser = Parser(sys.argv[1])

  if len(sys.argv) > 1: #fixxxxxx
    S = Scanner(sys.argv[2]) #gets the data file to handle input class
  inputData = [] #gets data from input file
  #gets the constants one by one from the input data file and appends to an array that will get passed to the execute function
  while S.currentToken() != Core.EOF:
    if S.currentToken() == Core.CONST:
      val = S.getCONST()
      inputData.append(val)
      S.nextToken()

  p = Program()
  p.parse(parser)
  p.execute(parser, inputData)
  # p.semantic(parser)
  # p.print()

if __name__ == "__main__":
    main()