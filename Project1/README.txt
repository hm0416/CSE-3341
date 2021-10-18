Name: Hifa Mousou

Files submitting:
Core.py - the ENUMS
Main.py - Calls the scanner, parses the program, and executes the program
Scanner.py - Professors Scanner.py
README.txt - Documentation of files included and any comments about the project.
Non-terminals as classes:
These classes listed below are all the non-terminals in the grammar. Each class contains an init method, parse method, semantic method, print method, and execute method.

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
If.py
Input.py
Loop.py
Output.py
Stmt.py
StmtSeq.py
Term.py
Program.py

Id.py - professors class that he made, but i added a new method called setValOfID and an execute method
globals.py - a bunch of global variables that are used throughout my code to easily change variable values

Special features/comments: N/A

Description of overall design of the interpreter: The interpreter executes instructions. In order to do this, a lexer (scanner) is created
to get the tokens from an input file, then the source code needs to be parsed and checked for any semantic/syntax errors and a parse tree is created
from this. Next, the interpreter takes this parse tree and executes it using the execute method that's in every class and the execute method
uses recursive descent to execute the statements/expressions.

How I tested the interpreter:
I made a test file and would test out different programs to see where the code breaks or where errors get printed. I also set breakpoints
throughout my parser when I encountered any bugs.

Known Bugs/issues: The last 4 test cases do not work. I believe there is an issue with my nested scoping. I tried re-doing the program and using
3 regions of memory (so making a static, stack and heap out of a list of dictionaries -- having 3 separate ones) but that also did not work for me.

