from Parser import Parser
from Program import Program
import globals

import sys

def main():
  #initializes globals.py class so globals can be used throughout my program
  globals.initialize()
  # Initialize the parser object (contains the scanner and some helper functions)
  parser = Parser(sys.argv[1])
  p = Program()
  p.parse(parser)
  p.execute(sys.argv[2])


if __name__ == "__main__":
    main()