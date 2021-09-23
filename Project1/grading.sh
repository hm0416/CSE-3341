#!/bin/bash


longest_common_prefix () {
  local prefix= n
  ## Truncate the two strings to the minimum of their lengths
  if [[ ${#1} -gt ${#2} ]]; then
    set -- "${1:0:${#2}}" "$2"
  else
    set -- "$1" "${2:0:${#1}}"
  fi
  ## Binary search for the first differing character, accumulating the common prefix
  while [[ ${#1} -gt 1 ]]; do
    n=$(((${#1}+1)/2))
    if [[ ${1:0:$n} == ${2:0:$n} ]]; then
      prefix=$prefix${1:0:$n}
      set -- "${1:$n}" "${2:$n}"
    else
      set -- "${1:0:$n}" "${2:0:$n}"
    fi
  done
  ## Add the one remaining character, if common
  if [[ $1 = $2 ]]; then prefix=$prefix$1; fi
  printf %s "$prefix"
}

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

fullpoints="Output fully matches: "
halfpoints="At least half matches: "
nopoints="Less than half matches: "

for value in {1..26}
do
	echo ""
	echo "Running ${value}.code"
	timeout 5 ${runner} Correct/${value}.code > Correct/${value}.student
	#Check for correct print
	tr -d '[:space:]' < Correct/${value}.student > temp1
	tr -d '[:space:]' < Correct/${value}.code > temp2
	if cmp -s "temp1" "temp2"; 
	then
		echo "Print looks good"
		score=$(($score + 1))
		fullpoints+=" "
		fullpoints+=${value}
	else
		student=$(<temp1)
		correct=$(<temp2)
		prefix=$(longest_common_prefix "$student" "$correct");
		prefixlength=$((${#prefix}))
		correctlength=$((${#correct}))
		missing=$(($correctlength - $prefixlength))
		if [[ $prefixlength -gt $missing ]] 
		then
			echo "First half of print looks good"
			halfpoints+=" "
			halfpoints+=${value}
		else
			echo "Student output and expected output are different"
			nopoints+=" "
			nopoints+=${value}
		fi
	fi
done

rm temp1
rm temp2

echo "Running error cases:"
echo ""
echo "Running 01.error:"
timeout 5 ${runner} Error/01.code
read -n 1 -p "Error is ++ in expression. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	echo -e "\nscore updated"
	error=$(($error + 1))
else
	echo -e "\nscore NOT updated"
	errorcases+=" "
	errorcases+="01"
fi
echo ""
echo "Running 02.error:"
timeout 5 ${runner} Error/02.code
read -n 1 -p "Error is y variable undeclared. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	echo -e "\nscore updated"
	error=$(($error + 1))
else
	echo -e "\nscore NOT updated"
	errorcases+=" "
	errorcases+="02"
fi
echo ""
echo "Running 03.error:"
timeout 5 ${runner} Error/03.code
read -n 1 -p "Error is 'x' variable declared twice in same scope. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	echo -e "\nscore updated"
	error=$(($error + 1))
else
	echo -e "\nscore NOT updated"
	errorcases+=" "
	errorcases+="03"
fi
echo ""
echo "Running 04.error:"
timeout 5 ${runner} Error/04.code
read -n 1 -p "Error is endif missing. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	echo -e "\nscore updated"
	error=$(($error + 1))
else
	echo -e "\nscore NOT updated"
	errorcases+=" "
	errorcases+="04"
fi
echo ""
echo "Running 05.error:"
timeout 5 ${runner} Error/05.code
read -n 1 -p "Error is assign in condition. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	echo -e "\nscore updated"
	error=$(($error + 1))
else
	echo -e "\nscore NOT updated"
	errorcases+=" "
	errorcases+="05"
fi
echo ""
echo "Running 06.error:"
timeout 5 ${runner} Error/06.code
read -n 1 -p "Error is endif instead of endwhile. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	echo -e "\nscore updated"
	error=$(($error + 1))
else
	echo -e "\nscore NOT updated"
	errorcases+=" "
	errorcases+="06"
fi
echo ""
echo "Running 07.error:"
timeout 5 ${runner} Error/07.code
read -n 1 -p "Error is ids after end. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	echo -e "\nscore updated"
	error=$(($error + 1))
else
	echo -e "\nscore NOT updated"
	errorcases+=" "
	errorcases+="07"
fi
echo ""
echo "Running 08.error:"
timeout 5 ${runner} Error/08.code
read -n 1 -p "Error is int variable used in 'id = ref id' assignment. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	echo -e "\nscore updated"
	error=$(($error + 1))
else
	echo -e "\nscore NOT updated"
	errorcases+=" "
	errorcases+="08"
fi
echo ""
echo "Running 09.error:"
timeout 5 ${runner} Error/09.code
read -n 1 -p "Error is missing semicolon. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	echo -e "\nscore updated"
	error=$(($error + 1))
else
	echo -e "\nscore NOT updated"
	errorcases+=" "
	errorcases+="09"
fi
echo ""
echo "Running 10.error:"
timeout 5 ${runner} Error/10.code
read -n 1 -p "Error is missing right parenthesis. Error message related to that? (y/n)" mainmenuinput
if [ $mainmenuinput = "y" ]; then
	echo -e "\nscore updated"
	error=$(($error + 1))
else
	echo -e "\nscore NOT updated"
	errorcases+=" "
	errorcases+="10"
fi

echo ""
echo "REPORT:"
echo $fullpoints
echo $halfpoints
echo $nopoints
echo $errorcases
echo ""
echo "Count of correct cases (out of 26):"
echo $score
echo "Count of error cases (out of 10):"
echo $error

echo "Done!"