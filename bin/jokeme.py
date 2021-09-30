#!/usr/bin/python3
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
# Requirements:
#	/usr/bin/python3 -m pip install requests
#	/usr/bin/python3 -m pip install ratelimiter
#
#############################################################################
#############################################################################
# Modification Information:
#   09/28/2021  JAC Initial Release
#   09/29/2021  JAC Switched from curl to requests for http calls.
#               JAC Added a ratelimiter.
#############################################################################

import subprocess, os, sys, requests, time
from os import system, name 
from ratelimiter import RateLimiter

#############
# VARIABLES #
#############
RUND = os.path.dirname(__file__)
INPUTD = RUND + '/../input'
INPUTF = "dadjokes_ids.txt"
INPUT = INPUTD + '/' + INPUTF
sub = "not found"
url = 'https://icanhazdadjoke.com/j'
HEAD = {'User-Agent':'MyLibrary (https://github.com/JamesCouncilTN/GitTheJob)' ,  'Accept':'text/plain'}

#############
# FUNCTIONS #
#############
#------------------------------------------------------
# Function to clear the screen.
#
def clearScreen(): 
 if name == 'nt': 
  _ = system('cls') 
 else: 
  _ = system('clear') 

#------------------------------------------------------
# Function to pause the API calls to a defined maximum.
#
def limited(until):
 duration = int(round(until - time.time()))
 print('Rate limited, sleeping for {:d} seconds'.format(duration))

#############################################
# Start
#############################################
rate_limiter = RateLimiter(max_calls=100, period=60, callback=limited)

clearScreen()
infile = open(INPUT, 'r')
IDS = list(infile)
for id in IDS:
 with rate_limiter:
  ID = id.strip()
  URL = url + '/' + ID
  rep = requests.get(URL, headers=HEAD)
  Joke = rep.text
  if sub in Joke:
   JOKE = "[Dad joke not found]"
  else:
   JOKE = "<" + Joke + ">"
  print("<" + ID + ">" + " : " + JOKE)
#############################################
# Finish
#############################################
