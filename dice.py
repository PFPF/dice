#! /usr/bin/env python
# 2 Write a die simulation program

from pf import *

print("This program simulates rolling several dice.\nThe user can choose how many dice are rolled and how many sides of each dice.")
numDices = iinp("How many dices would you like to roll?")

for i in range(1, numDices + 1):
	sides = iinp("How many sides on die #{}?\n".format(i))
	print "The Die shows: ".format(i) + str(randint(1, sides))