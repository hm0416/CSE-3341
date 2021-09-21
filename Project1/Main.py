import symtable

from Scanner import Scanner
import sys
from Prog import Prog


def main():
    S = Scanner(sys.argv[1])
    symbolTableGlobal = []
    symbolTableLocal = []

    root = Prog()
    root.parse(S)
    root.semantic(symbolTableGlobal, symbolTableLocal)

    # for ele in symbolTableLocal:
    #     for ele2 in symbolTableGlobal:
    #         ele = str(ele)
    #         ele2 = str(ele2)
    #         if ele.isnumeric():
    #             continue
    #         elif ele.isalpha() and len(ele) == 1:
    #             if ele not in symbolTableGlobal:
    #                 print("ERROR: local variable " + ele + " is not declared")
    #                 quit()


    root.print(1)

if __name__ == "__main__":
    main()
