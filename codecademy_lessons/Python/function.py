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