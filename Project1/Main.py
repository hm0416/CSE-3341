from Parser import Parser
from Program import Program

import sys

def main():
  # Initialize the parser object (contains the scanner and some helper functions)
  parser = Parser(sys.argv[1])

  p = Program()
  p.parse(parser)
  p.execute(parser)
  # p.semantic(parser)
  # p.print()


if __name__ == "__main__":
    main()