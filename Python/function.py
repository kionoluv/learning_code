"""
=================
    FUNCTIONS
=================
"""
	#01 header: includes def keyword, name of the function, and any parameters function requires
	#02 comment: helps explains what the function does
	#03 body: describes procedures function carries out, is indented like conditionals

		def peanut_butter(): #header
			#prints 'JELLY' #comment
			print "JELLY" #body

"""
=========================
    CALL AND RESPONSE
=========================
"""
	#calling: after defining function, it must be called to be implemented

		def square(n): #n represents the
			"""returns square of a number"""
			squared = n**2
			print "%d squared is %d." % (n,squared)
			return squared
		square(10) #this calls the square function
	
	#parameter: acts as variable name for a passed in argument
	def square (n) #n is parameter of square
	def square (10) #called sqaure with argument of 10
		
		def power (base, exponent):
			result = base**exponent
			print "%d to the power of %d is %d." %(base, exponent, result)
		
		power (4, 5) #prints "4 to the power of 5 is 1024."
	
	#functions can call other functions
		def peanutButter(n):
			return n + 2
		
		def jelly(n):
			return peanutButter(n) * 13

"""
==============================
   PRACTICE YOUR FUNCTIONS
==============================
"""
def cube(number): #def function cube that takes argument called number
    return number**3 #returns the cube of number argument

def by_three(number): #def function by_three to take on argument called number

    if number % 3 == 0: #if number is divisible by three
        return cube(number) #calls cube(number) and returns cube(number)
    else: #if number is not divisible by three
        return False #return False

"""
=========================
    IMPORTING MODULES   
=========================
"""
#import this: importing a module
#module: file that contains definitions (includes variables and functions) that can be used once imported

	import math #imports python module math
	print math.sqrt(25) #import math and get sqrt() func from within math

#func import: imports certain variables or funcs from given module
	from math import sqrt

#universal import (import *): imports all variables and funcs from module, no need to .module for each line
	from math import *
	
	#remark:be careful using universal imports as they fill program with ton of varis and funcs
		#note: you can have two different funcs with the same name

"""
==========================
    BUILT-IN FUNCTIONS
==========================
"""
#built-in funcs in Python
	#.upper()
	#.lower()
	#.str()
	#.len()

#max() :takes any number of arguments and returns largest values
	maximum = max(2, 3, 45) #will select 45 b/c it is largest value
	print maximum #print 45

#min() :returns smallest value of given series of arguments
	minimum = min(-23, 3, 4) #will select -23 b/c it is smallest value
	print minimum #prints -23

#abs() :returns the absolute value of number, always returns a positive number
	absolute = abs(-349587)
	print absolute #print 349587

#type() :returns the type of data it receives as an argument
	print type(543) #prints <type 'int'>
	print type(938457.987) #prints <type'float'>
	print type('ayyyy') #prints <type 'str'>
	
"""
======================
    SECTION REVIEW
======================
"""
#REVIEW FUNCTIONS
def meow_meow(cat):
	if cat == "yes":
		return "Good little booboo!"
	
	elif cat == "no":
		return "BOOBOO WHAT'S WRONG."
	
	else:
		return "I can't help you little booboo..."
		
#REVIEW MODULES
import math
print math.sqrt(64) #prints 8.0

#REVIEW BUILT-IN FUNCTIONS
def sneeze_how_far(achoo):
	if type(achoo) == nt or type(achoo) == float:
		return abs(achoo)
	else:
		return "god bless"
