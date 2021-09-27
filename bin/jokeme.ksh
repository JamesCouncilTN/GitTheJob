#!/bin/ksh
#set -x

INPUTD=$(echo `dirname $0`"/../input")
INPUTF=dadjokes_ids.txt
INPUT=$INPUTD/$INPUTF
HEAD="User-Agent : MyLibrary (https://github.com/JamesCouncilTN/GitTheJob) text/plain"
BIN="curl -H \"$HEAD\" https://icanhazdadjoke.com/j"

clear
for ID in `cat $INPUT`
do
 joke=$($BIN/$ID 2>/dev/null)
 if echo $joke | grep -q "not found"; then
  JOKE="[Dad joke not found]"
 else
  JOKE="<$joke>"
 fi
 echo -e "<$ID> : $JOKE"
done
