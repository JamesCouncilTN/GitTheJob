#!/bin/ksh
#set -x
#############################################################################
# UNLicensed Materials - Property of No One.
#
#
# (UC) UNCopyright No One 2021   No Rights Reserved
#############################################################################
#############################################################################
# jokeme.ksh    28 Sep 2021     James Allen Council (JAC)
#
# Version 1.0
#
# Description:
#   This script is used to grab specific jokes from a dad joke site.
#
#############################################################################
#############################################################################
# Modification Information:
#   09/28/2021  JAC Initial Release
#   09/30/2021  JAC Added ratelimit.
#############################################################################

#############
# VARIABLES #
#############
INPUTD=$(echo `dirname $0`"/../input")
INPUTF=dadjokes_ids.txt
INPUT=$INPUTD/$INPUTF
HEAD="User-Agent : MyLibrary (https://github.com/JamesCouncilTN/GitTheJob) text/plain"
BIN="curl -H \"$HEAD\" https://icanhazdadjoke.com/j"
RATE=100
SEC=60

#############
# FUNCTIONS #
#############

#----------------------------------------------------------------------------
# Function to count
#
Count (){
let COUNT=$COUNT+1
if [ $COUNT -ge $RATE ] && [ $DIFF -le $SEC ] ; then
 let SLEEP=$SEC-$DIFF
 echo -e "\t[-] Maximum API rate of $RATE in $SEC seonds hit. Sleeping for $SLEEP seconds."
 sleep $SLEEP
elif [ $COUNT -ge $RATE ] && [ $DIFF -gt $SEC ] ; then
 COUNT=0
 START=$(date "+%s")
fi
}

#----------------------------------------------------------------------------
# Function to get joke.
#
Get_Joke (){
joke=$($BIN/$ID 2>/dev/null)
if echo $joke | grep -q "not found"; then
 JOKE="[Dad joke not found]"
else
 JOKE="<$joke>"
fi
echo -e "<$ID>\t: $JOKE"
}

#############################################
# Start
#############################################
clear
START=$(date "+%s")
COUNT=0

for ID in `cat $INPUT|xargs`
do
 NOW=$(date "+%s")
 let DIFF=$NOW-$START
 Count
 Get_Joke
done
#############################################
# Finish
#############################################
