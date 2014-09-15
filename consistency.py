#!/bin/python2.7

# coding=utf-8
import socket, sys
import re
from struct import *
import string
import subprocess

header = "** HABIT " +  sys.argv[1]
with open("/home/rayenok/org/todo.org") as datafile:
    #Skip text before the beginning of the block
    for line in datafile:
        match_header = re.search('\*\*\sHABIT\s'+sys.argv[1]+'.*',line)
        if match_header:
            break
    #Look up for the clock section
    for line in datafile:
        match_clock = re.search('\s*:LOGBOOK:',line)
        if match_clock:
            break

    previous = ""
    for line in datafile:
        match_clock = re.search('\s*:END:',line)
        if match_clock:
            break
        else:
            matched_data = re.search('-\sState\s\"DONE\"\s+'+ \
                                    'from\s\"\w+\"\s+'+ \
                                    '\[(\d{4}\-\d{2}-\d{2})\s\w{3}\s\d{2}:\d{2}\]' \
                                    ,line.decode('utf-8'),re.UNICODE)
            if matched_data:
                current = matched_data.group(1)
                if current != previous:
                    print current + " 1"
                    previous = current
