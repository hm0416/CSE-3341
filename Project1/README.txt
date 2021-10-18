Name: Hifa Mousou

Files submitting:
Core.py - the ENUMS
Main.py - Calls the scanner, parses the program, and executes the program
Scanner.py - Professors Scanner.py
README.txt - Documentation of files included and any comments about the project.
Non-terminals as classes:
These classes listed below are all the non-terminals in the grammar. Each class contains a parse method, semantic method, print method, and execute method.
Other methods may be included as well (some from the professors project 2 code and some are mine (such as the execute methods and the setValOfID method)).
Each class parses/executes the non-terminal that's specified in the grammar.

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

Id.py - The professors class that he made, but i added a new method called setValOfID and an execute method
globals.py - a bunch of global variables that are used throughout my code to easily change variable values. Each variable
has a comment next to it in the globals.py file. More details in that file.

Special features/comments: N/A

Description of overall design of the interpreter: The interpreter executes instructions. In order to do this, a lexer (scanner) is created
to get the tokens from an input file, then the source code needs to be parsed and checked for any semantic/syntax errors and a parse tree is created
from this. Next, the interpreter takes this parse tree and executes it using the execute method that's in every class and the execute method
uses recursive descent to execute the statements/expressions. If my program would have worked correctly with the three regions of memory (heap, stack, static)
then what would have happened is the global variables would get stored in static memory, the local variables in the stack, and then when a variable is
assigned the 'new' keyword, a new spot would be created in the heap for that variable and it would be initialized to zero. Then, if a variable on the LHS
of an expression would be assigned a ref of another variable, the variable on the LHS would point to the referenced variable on the RHS that's
in the heap to get its value. The stack would then update the value of the LHS variable to equal the index of the referenced variable in the heap, so this
allows the LHS variable to act as a 'pointer' to the variable on the RHS.

How I tested the interpreter:
I made a test file and would test out different programs to see where the code breaks or where errors get printed. I also set breakpoints
throughout my execute methods when I encountered any bugs. Sometimes I may have had to set breakpoints for the parser method.

Known Bugs/issues: The last 4 test cases that were given to us do not work. I believe there is an issue with my nested scoping. I tried re-doing my program and using
3 regions of memory (so making a static, stack and heap out of a list of dictionaries -- having 3 separate list of dictionaries) but that also did not work for me.
I tried a variety of different things to make it work but nothing seemed to work. The nested scopes worked fine in the other test cases, but
when a ref gets declared inside the nested scope that's when bugs occur that I do not know why/what is causing them :(. I tried my best to get it working
-- spent easily 15+ hours debugging/re-writing my code (excluding the 8-10 hours of writing the actual code).

