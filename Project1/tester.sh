#!/bin/bash

runner=$1

if test -f Main.py
then
	runner="python3.7 Main.py"
elif test -f Main.java
then
	echo "Attempting to compile..."
	javac *.java
	runner="java Main"
fi

for value in {0..9}
do
	echo ""
	echo "Running ${value}.code"
	timeout 5 ${runner} Correct/${value}.code Correct/${value}.data > Correct/${value}.student
	echo "Running diff with ${value}.expected"
	grep -o '[[:digit:]]\+' Correct/${value}.student > Correct/temp1
	grep -o '[[:digit:]]\+' Correct/${value}.expected > Correct/temp2
	if cmp -s "Correct/temp1" "Correct/temp2"; then
		echo "Print looks good"
		score=$(($score + 1))
	else
		echo "Student output and expected output are different"
	fi
done

rm Correct/temp1
rm Correct/temp2

echo ""
echo "Running error cases:"
echo ""

echo "Running 00.error:"
timeout 5 ${runner} Error/00.code Error/00.data
read -n 1 -p "Error function body missing (no stmt-seq). Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	error=$(($error + 1))
fi
echo ""
echo ""

echo "Running 01.error:"
timeout 5 ${runner} Error/01.code Error/01.data
read -n 1 -p "Error is bad function call (begin keyword appears twice in declaration of A). Probably caught as expected LPAREN, recieved ASSIGN. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	error=$(($error + 1))
fi
echo ""
echo ""

echo "Running 02.error:"
timeout 5 ${runner} Error/02.code Error/02.data
read -n 1 -p "Error is bad function declaration (extra ')'). Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	error=$(($error + 1))
fi
echo ""
echo ""

echo "Running 03.error:"
timeout 5 ${runner} Error/03.code Error/03.data
read -n 1 -p "Error is bad function call (missing ';'). Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	error=$(($error + 1))
fi
echo ""
echo ""

echo "Running 04.error:"
timeout 5 ${runner} Error/04.code Error/04.data
read -n 1 -p "Error is bad function declaration (empty formals list) Probably caught as expected ID, recieved RPAREN. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	error=$(($error + 1))
fi
echo ""
echo ""

echo "Running 05.error:"
timeout 5 ${runner} Error/05.code Error/05.data
read -n 1 -p "Semantic error, function call has no target. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	error=$(($error + 1))
fi
echo ""
echo ""

echo "Correct cases score out of 10:"
echo $score
echo "Error cases score out of 6:"
echo $error

echo "Done!"