"""
CODECADEMY: INTRO TO PYTHON

this document contains definitions of terms,
remarks on things I noticed/learned,
and notes on what the console prints and what the code does
"""

"""VARIABLES"""
#remark variables: stores a piece of data and gives it a name
my_variable = 10
#remark: this doesn't print anything in the console except for the text 'none'
my_favoriteNumberA = 2
my_favoriteNumberB = 11

"""BOOLEAN"""
#remark boolean: can use variables to store booleans true/false
my_boolean = True
my_int = 7
my_float = 1.25

"""REASSIGNING VARIABLES"""
my_favoriteNumberA = 2
my_favoriteNumberA = 11
#remark: will print 11 in the console
print my_favoriteNumberA

"""WHITSPACE"""
#error "IndentationError: expected an indented block": this error appears whnever whitespace is off
def spam():
#remark: IndentationError for the two lines below
eggs = 12
return eggs

print spam()

def spamA():
	#note: fixed the IndentationError by indenting the lines by 4 spaces
	eggsA = 12
	return eggsA

#note: prints 12
print spamA()

"""INTERPRETATION"""
#def interpreter: runs code line by line and checks for errors
waffles = True
pancakes = False

"""MATHEMATICS"""
addition = 1 + 2
subtraction = 4 - 3
multiplication = 5 * .6
division = 24 / 8

i_can_math = 4 * 6
#note: console will print 24
print i_can_math

#remark: in python, can combine math with other data types like booleans and commands to make useful programs

#def exponents: represented by **, so 2^2 would be written as 2**2
bread_crumbs = 10 ** 2
#note: console prints 100
print bread_crumbs

#remark: modulo is represented by %, refer to Java definition of modulo
hash_browns = 3 % 2
#prints 1
print hash_browns

