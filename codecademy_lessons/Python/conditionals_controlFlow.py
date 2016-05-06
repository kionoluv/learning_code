"""
CODECADEMY: PYTHON, CONDITIONALS & CONTROL FLOW
================================================
this document contains definitions of terms,
remarks on things I noticed/learned,
and notes on what the console prints and what the code does
"""

#def control flow: the ability to choose among outcomes based on what else is happening in program

"""
===========
COMPARATORS
===========
"""
	#remark: simpliest aspect of control flow
		#equal to ==
		#not equl to !=
		#less than <
		#less than equal to <=
		#greater than >
		#greater than equal to >=

	#remark: comparators compare is value ==/!=, >=, <= another variable
	#remark: == compared equality, whereas = assigns value to variable
		
		# Set this to True if 17 < 328 or to False if it is not.
		bool_oneA = True   # We did this one for you!

		# Set this to True if 100 == (2 * 50) or to False otherwise.
		bool_twoA = True

		# Set this to True if 19 <= 19 or to False if it is not.
		bool_threeA = True

		# Set this to True if -22 >= -18 or to False if it is not.
		bool_fourA = False

		# Set this to True if 99 != (98 + 1) or to False otherwise.
		bool_fiveA = False


		# (20 - 10) > 15
		bool_oneB = False    # We did this one for you!

		# (10 + 17) == 3**16
		# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
		bool_twoB = False

		# 1**2 <= -1
		bool_threeB = False

		# 40 * 4 >= -4
		bool_fourB = True

		# 100 != 10**2
		bool_fiveB = False

#remark: comparisons result in either true/false (boolean!)
		
		# Make me true!
		bool_oneC = 3 < 5  # We already did this one for you!

		# Make me false!
		bool_twoC = 2 ** 3 < 1 ** 2
			print bool_twoC

		# Make me true!
		bool_threeC = 4 >= 2
			print bool_threeC

		# Make me false!
		bool_fourC = 5 <= 3
			print bool_fourC

		# Make me true!
		bool_fiveC = 24 == (4 * 6)
			print bool_fiveC

"""
=================
BOOLEAN OPERATORS
=================
"""

	""" AND """

		#True and True is True
		#True and False is False
		#False and True is False
		#False and False is False

			bool_oneD = False and False
				print bool_oneD

			bool_twoD = -(-(-(-2))) == -2 and 4>= 16**0.5
				print bool_twoD

			bool_threeD = 19 % 4 != 300 / 10 / 10 and False
				print bool_threeD

			bool_fourD = -(1**2) < 2**0 and 10 % 10 <= 20 -10 * 2
				print bool_fourD

			bool_fiveD = True and True
				print bool_fiveD

	""" OR """

		#True or True is True
		#True or False is True
		#False or True is True
		#False or False is False

			bool_oneE = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'
				print bool_oneE

			bool_twoE = True or False
				print bool_twoE

			bool_threeE = 100**0.5 >= 50 or False
				print bool_threeE

			bool_fourE = True or True
				print bool_fourE

			bool_fiveE = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
				print bool_fiveE

	""" NOT """

		#Not True is False
		#Not False is True

			bool_oneF = not True
				print bool_oneF

			bool_twoF = not 3**4 < 4**3
				print bool_twoF

			bool_threeF = not 10 % 3 <= 10 % 2
				print bool_threeF

			bool_fourF = not 3**2 + 4**2 != 5**2
				print bool_fourF

			bool_fiveF = not not False
				print bool_fiveF

# remark: order that boolean operators are read: 
	# 1 not
	# 2 and
	# 3 or

bool_oneG = False or not True and True
	print bool_oneG

bool_twoG =  False and not True or True
	print bool_twoG

bool_threeG = True and not (False or False)
	print bool_threeG

bool_fourG = not not True or False and not True
	print bool_fourG

bool_fiveG = False or not (True and True)
	print bool_fiveG

# Use boolean expressions as appropriate on the lines below!
	#use some combination of boolean operators. use each one at least once

# Make me false!
bool_oneH = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_twoH = (4 > 2) or (5 < 4)

# Make me false!
bool_threeH = not 2**3 == 8

# Make me true!
bool_fourH = 6 * 4 and 3 * 4 == 12

# Make me true!
bool_fiveH = not (5 * 4 == 24)

"""
==================================
    CONDITION STATEMENT SYNTAX    
==================================
"""

	""" IF """
	#def if: conditional that executes specified code if expression is true
		
		response = 'Y'

		answer = "Left"
		if answer == "Left":
	    	print "This is the Verbal Abuse Room, you heap of parrot droppings!"
	    
	# Will the above print statement print to the console?
	# Set response to 'Y' if you think so, and 'N' if you think not.
	
	""" ELSE """
	#else complements the if statement
	#if expression is true, then run the if-block, if its flase then run the else-block

	""" ELIF """
	# def elif: short for 'else if'
	#If following statement is true, then run this elif-block

		def greater_less_equal_5(answer):
	    if answer > 5:
	        return 1
	    elif answer < 5:          
	        return -1
	    else:
	        return 0
	        
		print greater_less_equal_5(4)
		print greater_less_equal_5(5)
		print greater_less_equal_5(6)

"""
======================
    SECTION REVIEW
======================
"""

#COMPARATORS
	1 < 2
	4 > 3
	5 <= 6
	8 >= 7
	9 != 10
	11 == 11

#BOOLEAN OPERATORS
	#Not True is False
	#Not False is True

	#True and True is True
	#True and False is False
	#False and True is False
	#False and False is False

	#True or True is True
	#True or False is True
	#False or True is True
	#False or False is False

	

#CONDITIONAL STATEMENTS
	if this_might_be_true():
			print "This really is truuu~"
	elif that_might_be_true():
			print "That is truuu~"
	else:
		print "Ayyyy lmao"

"""
======================================
    END OF SECTION PRACTICE REVIEW
======================================
"""

"""
GOALS:
- must include is, elif, and else
- at least one and, or, not
- a comparator
- the_flying_circus must return True
* the_flying_circus shouldn't have an argument (an input in the parentheses)
"""
	def the_flying_circus():
	    if not 6 >= 24 or 6 < 12:
	        return True
	    elif 6 == 2 * 3 or 6 >= 5:
	        return True
	    else:
	        return True

	print the_flying_circus()
