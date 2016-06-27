"""
=============================
    LISTS AND DIRECTORIES
=============================
"""

# LISTS #
	#lists (a datatype) stores different pieces of info as sequence under a single variable name
	#assign items to list:
		list_name = [item_1, item_2] #items listed between hard brackets
		empty_list = [] #lists can also be empty
	
	my_cravings = ["ice cream", "bubble tea", "berry-ful pancakes", "milkshake"];
		if len(my_cravings) >= 3:
			print "I really want some" + my_cravings[0]
				#i really want some ice cream
			print "I can't wait to have some" + my_cravings[1]
				#i can't wait to have some bubble tea
			print "It's been a long time since I made some" + my_cravings[2]
				#it's been a long time since I made some berry-ful pancakes
			print "Sometimes I just want a rich and delicious" + my_cravings[3]
				#sometimes i just want a rich and delicious milkshake
# INDEX #
	#index: identifies an item's place in the list
	#list indices begin at 0 and not 1
		letters = ["a", "b", "c", "d", "e"]
		print letter[0] #prints a
		print letter[2] #prints c
		print letter [4] #prints e
		print letter [1, 3] #prints bd

	#assignment: assigning another value to the list index
		letters2 = ["f", "g", "h", "i", "j"]
		letters2[0] = "k" #replaces "f" with "k"
		letters2[3] = "l" #replaces "i" with "l"
