#! python3
# printTable.py - Displays the contents of a list of lists of strings in a table format right justified

#List containing list of strings
#rows are downward
#columns are upward
tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]
			 
#Prints the list containing list containing strings
#table is the passed list
#numRows is the number of rows in table
#numCols is the number of columns in the table
def print_Table(table, numRows, numCols):
	
	#For loop to get the widths for each column
	#Widths stored in colWidths
	max = 0
	for list in tableData:
		for item in list:
			if len(item) > max:
				max = len(item)
				
	#Code used in a previous program (Chapter 4 - GridPicture) to do the display portion
	line = ''
	
	for r in range(numRows):
		for c in range(numCols):
			line += table[c][r].rjust(max)
		print(line)
		line = ''
	
#Test case
print_Table(tableData, len(tableData[0]), len(tableData))