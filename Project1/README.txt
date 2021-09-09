Name: Hifa Mousou

Files submitting:
Core.py - the ENUMS
Main.py - Calls scanner constructor and makes the tokenized list using my tokenizer function.
Scanner.py - Includes original methods plus a tokenizer method I created to tokenize all items in the input file.
README.txt - Documentation of files included and any comments about the project.

Special features/comments: My Scanner constructor does not call nextToken(). The way I initially setup my program made it so
I can't call nextToken in the scanner constructor. I've tried refactoring, but my program broke because of it, so I have left out the
method call to nextToken() in the scanner constructor.

Known Bugs: For some unknown reason, if you make a blank file and just put an EQUAL sign "=" or multiple without a newline at the end of the file,
the program halts and doesn't do anything. But if you put equal signs with a space, any other chars, or a newline, it works normally. I'm not sure if this
is something that will get tested, but the EQUAL sign works just fine otherwise.