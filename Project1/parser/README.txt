Name: Hifa Mousou

Files submitting:
Core.py - the ENUMS
Main.py - Calls the scanner, parses the program, and prints out the program
Scanner.py - Professors Scanner.py
README.txt - Documentation of files included and any comments about the project.
Non-terminals as classes:
These classes listed below are all the non-terminals in the grammar. Each class contains an init method, parse method, and print method.

Assign.py
Cmpr.py
Cond.py
Decl.py
DeclClass.py
DeclInt.py
DeclSeq.py
Expr.py
Factor.py
IdList.py
IF.py
IN.py
Loop.py
OUT.py
Stmt.py
StmtSeq.py
Term.py
Prog.py

Special features/comments: N/A

Description of overall design of the parser: The parser calls the Scanner to get the tokens that the scanner generates. The parser then
creates a parse tree with these tokens. This tree then gets passed to the semantic function to perform a semantic analysis. I made all the
non-terminals in the grammar be classes.

How I tested the parser:
I made a test file and would test out different programs to see where the code breaks or where errors get printed. I also set breakpoints
throughout my parser when I encountered any bugs.

Known Bugs/issues: I was not able to get to the semantic function to work. The farthest I got was being able to setup a list of dictionaries.
What I did was create a symbolTable variable in main and declared it as a list of dictionaries, then passed it to the semantic function. In
each semantic function, I recursively called the semantic functions for the other classes. The majority of the error handling would've been
completed in the ASSIGN, FACTOR, IDLIST, INPUT, DeclInt, DeclClass classes.
