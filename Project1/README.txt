Name: Hifa Mousou

Files submitting:
Core.py - the ENUMS
Main.py - Initialized my globals.py class, calls the scanner, parses the program, and executes the program
Scanner.py - Professors Scanner.py
README.txt - Documentation of files included and any comments about the project.
Non-terminals as classes:
These classes listed below are all the non-terminals in the grammar. Each class contains a parse method and execute method.
Other methods may be included as well (some from the professors project 2/3 code and some are mine (such as the execute methods in FuncCall.py, FuncDecl.py, and Formals.py and the semantic method in FuncCall.py and FuncDecl.py)).
Each class parses/executes the non-terminal that's specified in the class name and in the grammar.

Assign.py
Cmpr.py
Cond.py
Decl.py
DeclClass.py
DeclInt.py
DeclSeq.py
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
Stmt.py
StmtSeq.py
Term.py
Program.py
Parser.py

globals.py - Global variables that are used throughout my code to easily change variable values. Each variable
has a comment next to it in the globals.py file. More details in that file.

Special features/comments: N/A

Description of overall design of the interpreter: The interpreter executes instructions. In order to do this, a lexer (scanner) is created
to get the tokens from an input file, then the source code needs to be parsed and checked for any semantic/syntax errors and a parse tree is created
from this. Next, the interpreter takes this parse tree and executes it using the execute method that's in every class and the execute method
uses recursive descent to execute the statements/expressions. The global variables get stored in static memory, the local variables in the stack, and then when a variable is
assigned the 'new' keyword, a new spot would be created in the heap for that variable and it would be initialized to zero. Then, if a variable on the LHS
of an expression would be assigned a ref of another variable, the variable on the LHS would point to the referenced variable on the RHS that's
in the heap to get its value. The stack would then update the value of the LHS variable to equal the index of the referenced variable in the heap, so this
allows the LHS variable to act as a 'pointer' to the variable on the RHS. For the functions, a new stack gets created. The function name and its definition get
added to this stack. In my code, the function name maps to the function definition. In general, a new stack frame is created for each function. When a function is called, its arguments are pushed onto the stack that gets created. Once the
function returns, the arguments are then popped off the stack.

How I tested the interpreter:
I made a test file and would test out different programs to see where the code breaks or where errors get printed. I also set breakpoints
throughout my execute methods when I encountered any bugs. Sometimes I may have had to set breakpoints for the parser method.

Known Bugs/issues:

My semantic check for "checking that the formal parameters of a function are distinct from each other" works when there is only one function declaration,
but when there is more than one, it seems like my program only looks at the lastly declared function and looks at whether the formal parameters for that
last function are distinct or not, and ignores any functions declared before the last one. So if any functions declared before the last one have parameters
of the same name, it wont recognize it and it won't throw an error. I tried several ways of fixing this, such as trying to keep track of the parameters
for each function but that didn't seem to work :-(.

