#! python3
# strongPassword.py - Program to check if a password is strong
# A strong password is defined as follows:
# At least 8 characters long
# Contains both uppercase and lowercase characters
# Has at least 1 digit

#Program takes in an argument from the command line which will be the password tested
import re, sys

if(len(sys.argv) != 2):
	print("Usage: python strongPassword.py [Password]")
	sys.exit()

lengthRegex = re.compile(r'(\w){8}', re.VERBOSE)
caseRegex = re.compile(r'\w*[A-Z][a-z]\w*|\w*[a-z][A-Z]\w*', re.VERBOSE)
digitRegex = re.compile(r'\w*[0-9]\w*', re.VERBOSE)

test = sys.argv[1]

if(lengthRegex.search(test) == None or caseRegex.search(test) == None or digitRegex.search(test) == None):
	print("Not a strong password")
else:
	print(test + " is a strong password.")
