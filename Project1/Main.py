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

  if len(sys.argv) > 1:
    S = Scanner(sys.argv[2]) #gets the data file to handle input class
  inputData = []
  while S.currentToken() != Core.EOF:
    if S.currentToken() == Core.CONST:
      val = S.getCONST()
      inputData.append(val)
      S.nextToken()

  tempS = Scanner(sys.argv[1])
  inputID = None
  outputID = None
  while tempS.currentToken() != Core.EOF:
    if tempS.currentToken() == Core.INPUT:
      tempS.nextToken()
      inputID = tempS.getID()
    elif tempS.currentToken() == Core.OUTPUT:
      tempS.nextToken()
      if tempS.currentToken() == Core.ID:
        outputID = tempS.getID()
      elif tempS.currentToken() == Core.CONST:
        outputID = tempS.getCONST()
    else:
      tempS.nextToken()

  p = Program()
  p.parse(parser)
  p.execute(parser, inputData, inputID, outputID)
  # p.semantic(parser)
  # p.print()


if __name__ == "__main__":
    main()