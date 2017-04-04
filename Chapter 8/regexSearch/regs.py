#! python3
# regs.py - Searches through a folder's txt files and looks for matches to a regular expression
# USAGE: py.exe regs.py num - Checks if the text file contains any numbers
#		 py.exe regs.py help - Displays a list of commands for this script

import re, sys, os

def get_Path():
	path = input('Enter the absolute path to the folder:\n')
	path = path.replace('\\', '\\\\')
	try:
		os.chdir(path)
		fileList = os.listdir(path)
		delList = []
		for file in fileList:
			if(not file.endswith('.txt')):
				delList.append(file)
		for file in delList:
			fileList.remove(file)
		return fileList
	except FileNotFoundError:
		print("Path does not exist! Please enter a valid path.")
		sys.exit()

def file_Check(fileList, regex):

	updatedList = []
	for file in fileList:
		fileRead = open(file, 'r')
		fileContents = fileRead.read()
		check = regex.search(fileContents)
		
		if(check != None):
			updatedList.append(file)
			
	return updatedList
		
def basic_Usage():
	print('USAGE: py.exe regs.py <command>')
	print('Use -help as the command with no path to get a list of commands')
	sys.exit()

def help_Usage():
	print('\nUSAGE: py.exe regs.py <command>')
	print('\n<command>:\n')
	print('\t-num - Returns a list of text files from the desired folder that contain a number\n')
	print('\t-help - Displays a list of commands for the regs.py script\n')
	sys.exit()
	
def num_Regex():
	fileList = get_Path()
	regexNumber = re.compile(r'[0-9]', re.VERBOSE)
	
	return file_Check(fileList, regexNumber)
	
if len(sys.argv) != 2:
	basic_Usage()

else:
	if(sys.argv[1].lower() == '-num'):
		print(num_Regex())
	elif(sys.argv[1].lower() == '-help'):
		help_Usage()
	else:
		basic_Usage()