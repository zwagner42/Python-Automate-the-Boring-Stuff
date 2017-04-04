#! python3
# regexStrip.py - Program will contain a function to will strip a string using regexStrip

import re

#Function to strip characters from the beginning and end of a string using regex
#string is the string that is being stripped
#replace is a string containing the characters to strip away
def regex_Strip(string, replace):
	if replace == '':
		stripRegex = re.compile(r'^\s* | \s*$', re.VERBOSE)
		storage = stripRegex.sub('', string)
		return storage
	else:
		storage = string
		characterStorage = list(replace)
		for char in characterStorage:
			stripRegex = re.compile(r'^' + re.escape(char) + '* | ' + re.escape(char) + '*$', re.VERBOSE)
			storage = stripRegex.sub('', storage)
		return storage

#Test Cases
strippedString = regex_Strip('   Hello World ', '')
print(strippedString)
strippedString = regex_Strip('aaaHello Worldbb', 'ab')
print(strippedString)
strippedString = regex_Strip('I Love America So Much', 'IoL ')
print(strippedString)