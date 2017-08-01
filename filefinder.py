#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import os

#Files Finder - Developed by Panic | Greetz: WHK  ; D3l3v3 ; fr0n
#http://github.com/hck1army

#Usage:
#$ python filefinder.py http://www.domain.com

c_red	= 	"\033[01;31m"
c_green = 	"\033[01;32m"
c_def	=	"\033[0m"
files	=	['backup.sql', 'bck.txt', '.git/', 'vssver.scc', '.ext~', '.ext.swp', '.ext.swo', '.log', 'Desktop.ini', '.DS_Store', 'Thumbs.db', '.fuse_hidden', '.bkp', '.gitignore', '.php~']
link 	=	sys.argv[1]

def welcome():
	os.system("clear")
	print """\033[1m
 _____ _ _             _____ _           _
|  ___(_) | ___  ___  |  ___(_)_ __   __| | ___ _ __
| |_  | | |/ _ \/ __| | |_  | | '_ \ / _` |/ _ \ '__|
|  _| | | |  __/\__ \ |  _| | | | | | (_| |  __/ |
|_|   |_|_|\___||___/ |_|   |_|_| |_|\__,_|\___|_| 
                                                                 
  Developed by Panic. | Greetz: WHK ; D3l3v3 ; fr0n ;  (\033[0mhttp://www.github.com/hck1army\033[1m)\033[0m

"""

if len(sys.argv) > 2 or len(sys.argv) < 2:
	print "\n\033[1mUsage:\n$\033[0m %s %s\n" % (sys.argv[0], sys.argv[1])
elif "http" in link:
	welcome()
	for file in files:
		get_url	=	requests.get("%s/%s" % (link, file))
		if get_url.status_code != 200:
			print "%s  Failed :(	[%s]	:	%s/%s%s" % (c_red, get_url.status_code, link, file, c_def)
		else:
			print "%s  Success :)	[%s]	:	%s/%s%s" % (c_green, get_url.status_code, link, file, c_def)
else:
	print "\nYou used \033[1mHTTP?\033[0m\n"
