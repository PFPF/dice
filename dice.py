#! /usr/bin/env python
# 2 Write a die simulation program

from pf import *

numDices = iinp("How many dices would you like to roll?")
sides = iinp("How many sides on your die?")
for i in range(1, numDices + 1):
	print "Die {} shows: ".format(i) + str(randint(1, sides))