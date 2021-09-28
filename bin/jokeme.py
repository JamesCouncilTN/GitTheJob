#!/usr/bin/python
#set -x

import subprocess, os, sys
from os import system, name 

RUND = os.path.dirname(__file__)
INPUTD = RUND + '/../input'
INPUTF = "dadjokes_ids.txt"
INPUT = INPUTD + '/' + INPUTF
HEAD = "\"User-Agent : MyLibrary (https://github.com/JamesCouncilTN/GitTheJob) text/plain\""
BIN = "/usr/bin/curl -sH " + HEAD + " https://icanhazdadjoke.com/j"
sub = "not found"

def clearScreen(): 
 if name == 'nt': 
  _ = system('cls') 
 else: 
  _ = system('clear') 

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
