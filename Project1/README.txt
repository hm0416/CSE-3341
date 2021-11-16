Name: Hifa Mousou

Files submitting:
Core.py - the ENUMS
Main.py - calls the scanner, parses the program, and executes the program
Scanner.py - Professors Scanner.py
README.txt - Documentation of files included and any comments about the project.
Non-terminals as classes:
These classes listed below are all the non-terminals in the grammar. Each class contains a parse method, print method, and execute method.
I used the professor's project 4 code.
Each class parses/executes the non-terminal that's specified in the class name and in the grammar.

Assign.py
Cmpr.py
Cond.py
Decl.py
DeclClass.py
DeclInt.py
DeclSeq.py
Executor.py
Expr.py
Factor.py
Formals.py
FuncCall.py
FuncDecl.py
Id.py
IdList.py
If.py
Input.py
Loop.py
Output.py
StmtSeq.py
Term.py
Program.py
Parser.py

Special features/comments: N/A

How I tested the interpreter:
I made a test file and would test out different programs to see how the garbage collector acts in different situations. I also set breakpoints
throughout my execute methods when I encountered any bugs.

Known Bugs/issues: For the test cases 6.code and 8.code, they do not print correctly. 6.code prints off everything but the ordering
is messed up. It seems if there is a function call and then an output statement right after, there is an issue with the ordering
of the gc prints. 8.code printed an extra gc:0, which I wasn't too sure why it was doing that.

