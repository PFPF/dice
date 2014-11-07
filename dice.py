#! /usr/bin/env python
# 2 Write a die simulation program

from pf import *
sides = iinp("How many sides on your die?")
print "The die shows: " + str(randint(1, sides))