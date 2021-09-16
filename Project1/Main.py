from Project1.Scanner import Scanner
import sys
from Prog import Prog


def main():
    S = Scanner(sys.argv[1])
    root = Prog()

    root.parse(S)
    # root.semantic()
    root.print()

if __name__ == "__main__":
    main()
