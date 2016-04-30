"""
CODECADEMY: PYTHON, CONDITIONALS & CONTROL FLOW
================================================
this document contains definitions of terms,
remarks on things I noticed/learned,
and notes on what the console prints and what the code does
"""

#def control flow: the ability to choose among outcomes based on what else is happening in program

"""COMPARATORS"""
#remark: simpliest aspect of control flow
	#equal to ==
	#not equl to !=
	#less than <
	#less than equal to <=
	#greater than >
	#greater than equal to >=
#remark: comparators compare is value ==/!=, >=, <= another variable
#remark: == compared equality, whereas = assigns value to variable

		#Assign True or False as appropriate on the lines below!
		
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

""" ============================================================= """
		#Assign True or False as appropriate on the lines below!
		
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
		
		#Create comparative statements as appropriate on the lines below!
		
		# Make me true!
		bool_oneC = 3 < 5  # We already did this one for you!

		# Make me false!
		bool_twoC = 2 ** 3 < 1 ** 2

		# Make me true!
		bool_threeC = 4 >= 2

		# Make me false!
		bool_fourC = 5 <= 3

		# Make me true!
		bool_fiveC = 24 == (4 * 6)

"""AND"""
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

"""OR"""
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

"""NOT"""
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