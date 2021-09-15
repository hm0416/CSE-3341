from Project1.scanner.Scanner import Scanner
import sys
import Prog


def mainParser():
    S = Scanner(sys.argv[1])
    root = Prog

    root.parse(S)
    # root.semantic()
    root.print()

if __name__ == "__mainParser__":
    mainParser()
