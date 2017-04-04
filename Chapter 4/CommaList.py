#Sample program to display a list of values in comma separated format

#Function to print a given list in a comma separated format
#Takes a list to be printed in a comma separated format
def comma_List(passedList):
	#Message to be printed to the console
	message = ''
	
	if len(passedList) == 0:
		print('Empty List')
		
	elif len(passedList) == 1:
		print(passedList[0])
	else:
		#Loop through the list and add each element except for the last one to the message
		for i in range(len(passedList) - 1):
			message += passedList[i] + ', '
		message +=  'and ' + passedList[-1]
		print(message)

#Testing cases
test = ['apples', 'bananas', 'tofu', 'cats']
comma_List(test)
test2 = []
comma_List(test2)
test3 = ['one']
comma_List(test3)