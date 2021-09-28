#!/usr/bin/python
#############################################################################
# UNLicensed Materials - Property of No One.
#
#
# (UC) UNCopyright No One 2021   No Rights Reserved
#############################################################################
#############################################################################
# jokeme.py    28 Sep 2021     James Allen Council (JAC)
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
#############################################################################

import subprocess, os, sys
from os import system, name 

#############
# VARIABLES #
#############
RUND = os.path.dirname(__file__)
INPUTD = RUND + '/../input'
INPUTF = "dadjokes_ids.txt"
INPUT = INPUTD + '/' + INPUTF
HEAD = "\"User-Agent : MyLibrary (https://github.com/JamesCouncilTN/GitTheJob) text/plain\""
BIN = "/usr/bin/curl -sH " + HEAD + " https://icanhazdadjoke.com/j"
sub = "not found"

#############
# FUNCTIONS #
#############
def clearScreen(): 
 if name == 'nt': 
  _ = system('cls') 
 else: 
  _ = system('clear') 

#############################################
# Start
#############################################
clearScreen()
infile = open(INPUT, 'r')
IDS = list(infile)
for id in IDS:
 ID = id.strip()
 GET = BIN + '/' + ID + ' 2>/dev/null'
 joke = os.popen(GET)
 Joke = joke.read()
 if sub in Joke:
  JOKE = "[Dad joke not found]"
 else:
  JOKE = "<" + Joke + ">"
 print("<" + ID + ">" + " : " + JOKE)
#############################################
# Finish
#############################################
