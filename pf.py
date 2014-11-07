"""
	imports turtle, math, random that the user doesn't need to import them again.
	Defines classes and functions for special input.
	Defines classes and functions for 2D geometry objects.
	Defines class for vectors
"""

from turtle import *
from math import *
from random import *

def iinp(sent = "", isPositive = False, allowZero = False): # int_input
	'''
		Allow the user to input an integer (if not then let the user to try again)
	'''
	try:
		given = int(raw_input(sent))
	except:
		print("That's not a integer!")
		return iinp(sent, isPositive, allowZero)
	else:
		if(isPositive and (not allowZero) and given <= 0) or (isPositive and allowZero and given < 0):
			print("That's not positive!")
			return iinp(sent, isPositive, allowZero)
		else:
			return given

def finp(sent = "", isPositive = False, allowZero = False): # float_input
	'''
		Allow the user to input an float (if not then let the user to try again)
	'''
	try:
		given = float(raw_input(sent))
	except:
		print("That's not a integer!")
		return finp(sent, isPositive, allowZero)
	else:
		if(isPositive and (not allowZero) and given <= 0) or (isPositive and allowZero and given < 0):
			print("That's not positive!")
			return finp(sent, isPositive, allowZero)
		else:
			return given
		
def yninp(sent = "", true = 'y', false = 'n'): # yes_no_input
	'''
		Allow the user to input "yes" or "no" (or try again)
	'''
	string = raw_input(sent)
	if(string[0].lower() == true): # "yes"
		return True
	elif(string[0].lower() == false): # "no"
		return False
	else:
		print("ENTER YES OR NO PLEASE")
		return yninp(sent, true, false)
	
class vector(object):
	'''
		Vector classes are defined here: '+' '-' '*' 'magnitude' 'direction' are available
	'''
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self, anotherVector): # +
		return vector(self.x + anotherVector.x, self.y + anotherVector.y, self.z + anotherVector.z)
	# def __radd__(self, anotherVector): # +
		# try:
			# return self + anotherVector
		# except:
			# return self
		#return vector(self.x + anotherVector.x, self.y + anotherVector.y, self.z + anotherVector.z)
	def __sub__(self, anotherVector): # -
		return vector(self.x - anotherVector.x, self.y - anotherVector.y, self.z - anotherVector.z)
	def __neg__(self): # +/-
		return vector(-self.x, -self.y, -self.z)
	def __mul__(self, another):       # *
		if isinstance(another, (float, int)): # if "another" is a float or int
			return vector(self.x * another, self.y * another, self.z * another) # (3,5) * 3
		return self.x * another.x + self.y * another.y + self.z * another.z # v1.v2 = x1x2 + y1y2 + z1z2
	def __rmul__(self, another):      # being *ed
		if isinstance(another, (float, int)): 
			return vector(self.x * another, self.y * another, self.z * another) # 3 * (3,5)
		return self.x * another.x + self.y * another.y + self.z * another.z # v1.v2 = x1x2 + y1y2 + z1z2
		# Actually they are same...
	def __abs__(self): # magnitude ( |F| )
		return round(sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2), 2)
	def ddir(self): # degree direction, available if 2D
		return round(atan2(self.y, self.x) * 180 / pi, 1) # atan2 is a fantastic function

class point(object):
	'''
		Points' classes -- the user can draw it by the turtle.
	'''
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = z
	def __sub__(self, anotherPoint): # Two points make a vector
		return vector(self.x - anotherPoint.x, self.y - anotherPoint.y)
	def move(self, vect): # add a movement vector to the point
		self.x += vect.x
		self.y += vect.y
		self.z += vect.z
	def draw(self, init, isPenDown = False, color = "black", linecolor = "black", isHide = True, angle = 0, radius = 5): # DRAW it
		drawingTurtle = Turtle()
		drawingTurtle.speed(0)
		if(isHide): drawingTurtle.ht() # hide the turtle
		drawingTurtle.penup() # lift it up
		drawingTurtle.goto(init.x, init.y)
		if(isPenDown):
			drawingTurtle.pendown()
			drawingTurtle.dot(radius, color)
			drawingTurtle.pencolor(linecolor) # Set the pencolor "linecolor" to draw such line when "goto"
		drawingTurtle.setheading(angle)
		drawingTurtle.goto(self.x, self.y)
		drawingTurtle.dot(radius, color)


def vecsum(vectors):
	'''
	Calculate the sum of a list of vectors, with drawings
	'''
	pos = origin = point(0,0) # set the initial position
	for vector in vectors[1:]:
		x0 = pos.x; y0 = pos.y # "older" position
		pos.move(vector)
		pos.draw(point(x0, y0), True, "black", "black", False, vector.ddir()) # drawing
	vTotal = pos - origin
	pos.draw(origin, True, "red", "red", False, vTotal.ddir())
	return vTotal
	
class Circle(object):
	'''
		Geometry object -- circle (written in class -- not "class")
	'''
	def __init__(self, center = point(0, 0, 0), r = 1): # by the center and the radius
		self.c = center
		self.r = r
	def circuf(self): # circumference
		return 2 * pi * self.r
	def area(self): # area
		return pi * self.r ** 2