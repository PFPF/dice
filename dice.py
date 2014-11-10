#! /usr/bin/env python
# 2 Write a die simulation program

from pf import *

print("This program simulates rolling several dice.\nThe user can choose how many dice are rolled.\n") # Tell them what the program do

numDices = iinp("How many dices would you like to roll?\n", True) # positive integer only

for i in range(1, numDices + 1):
	while True:
		sides = iinp("How many sides on die #{}?\n".format(i), True) # positive integer only
		if(sides == 1): print("There's no object which has 1 side except 'Mobius band'.")
		else: break
	print "The Die shows: ".format(i) + str(randint(1, sides))
