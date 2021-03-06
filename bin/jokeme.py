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
#	/usr/bin/python3 -m pip install ratelimit
#	/usr/bin/python3 -m pip install backoff
#
#############################################################################
#############################################################################
# Modification Information:
#   09/28/2021  JAC Initial Release
#   09/29/2021  JAC Switched from curl to requests for http calls.
#               JAC Added a ratelimiter.
#   09/30/2021  JAC Switched from ratelimiter to ratelimit.
#               JAC Added backoff.
#############################################################################

import os, sys, requests, time
from os import system, name 
from ratelimit import limits, RateLimitException, sleep_and_retry
from backoff import on_exception, expo

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
ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 100

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
# Function to get jokes and pause the API calls to a
#	defined maximum.
#
#@sleep_and_retry
@on_exception(expo, RateLimitException, max_tries=8)
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def getjoke():
 rep = requests.get(URL, headers=HEAD)
 Joke = rep.text
 if sub in Joke:
  JOKE = "[Dad joke not found]"
 else:
  JOKE = "<" + Joke + ">"
 print("<" + ID + ">" + " : " + JOKE)

#############################################
# Start
#############################################
clearScreen()
infile = open(INPUT, 'r')
IDS = list(infile)
for id in IDS:
 ID = id.strip()
 URL = url + '/' + ID
 getjoke()
#############################################
# Finish
#############################################
