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

score=0
error=0

for value in {1..30}
do
	echo ""
	echo "Running ${value}.code"
	timeout 5 ${runner} Cases/Correct/${value}.code Cases/Correct/${value}.data > Cases/Correct/${value}.student
	echo "Running diff with ${value}.expected"
	grep -o '[[:digit:]]\+' Cases/Correct/${value}.student > temp1
	grep -o '[[:digit:]]\+' Cases/Correct/${value}.expected > temp2
	if cmp -s "temp1" "temp2"; then
		echo "Print looks good"
		score=$(($score + 1))
	else
		echo "Student output and expected output are different"
	fi
done

rm temp1
rm temp2

echo "Running error cases:"
echo ""
echo "Running 01.error:"
timeout 5 ${runner} Cases/Error/01.code Cases/Error/01.data
read -n 1 -p "Error is .data file not having enough values. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	error=$(($error + 1))
fi
echo ""
echo "Running 02.error:"
timeout 5 ${runner} Cases/Error/02.code Cases/Error/02.data
read -n 1 -p "Error is assignment to null ref variable. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	error=$(($error + 1))
fi

echo ""
echo "Correct cases score out of 30:"
echo $score
echo "Error cases score out of 2:"
echo $error
echo ""

echo "Done!"