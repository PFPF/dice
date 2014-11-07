#! /usr/bin/env python
# 2 Write a die simulation program

from pf import *

print("This program simulates rolling several dice.\nThe user can choose how many dice are rolled.") # Tell them what the program do

numDices = iinp("How many dices would you like to roll?", True) # positive integer only
sides = iinp("How many sides on your die?", True) # positive integer only

for i in range(1, numDices + 1):
	print "Die {} shows: ".format(i) + str(randint(1, sides))