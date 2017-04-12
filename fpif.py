#!/usr/bin/python
#
# fpif stands for Find Pattern Into a File
# It's a simple and silly stuff just to practice
#
# @guilty: Alan Lacarda aka alacerda
# @when: today (10/04/2017)
#

import sys

usage = """
	USAGE
	./fpif.py <filename> <pattern>

	filename - File where we will find the pattern
	pattern - Pattern we are searching in the given file

	EXAMPLE
	In order to search inside /var/log/messages file for the lines containning "usb" word:
		fpif /var/log/messages usb
"""

if (len(sys.argv) != 3):
	print usage
	quit()
try :
	fd = open(sys.argv[1],"r")
except IOError as e:
	print "We cold't find the specified file: %s"%sys.argv[1]
	print "Exiting with error: %s"%e
	quit()

def write_line(line):
	print line

for line in fd.readlines():
	if line.find(sys.argv[2]) != -1:
		write_line(line)

