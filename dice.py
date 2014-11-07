#! /usr/bin/env python
# 2 Write a die simulation program

from pf import *

numDices = iinp("How many dices would you like to roll?")

for i in range(1, numDices + 1):
	sides = iinp("How many sides on die #{}?".format(i))
	print "The Die shows: ".format(i) + str(randint(1, sides))