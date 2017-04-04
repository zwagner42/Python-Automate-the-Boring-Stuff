#Program to count the number of individual characters in a string with pretty dictionary

import pprint

#Counts the number of individual characters in a string
#Values stored in a dictionary 
def individual_Character_Count(string):
	count = {}
	
	for character in string:
		count.setdefault(character, 0)
		count[character] += 1
		
	pprint.pprint(count)

testString = "Hello my name is Dave.  I love people that agree with me and even thoughs who don't."
individual_Character_Count(testString)
