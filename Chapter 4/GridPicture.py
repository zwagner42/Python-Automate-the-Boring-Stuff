#Sample to print a list in the layout of a grid

#6x9 Grid (Rows are columns in this grid and vice versa)
#The length of the grid list is the number of columns
#The length of each sublist is the number of rows
grid = [['.', '.', '.', '.', '.', '.'],
		['.', '0', '0', '.', '.', '.'],
		['0', '0', '0', '0', '.', '.'],
		['0', '0', '0', '0', '0', '.'],
		['.', '0', '0', '0', '0', '0'],
		['0', '0', '0', '0', '0', '.'],
		['0', '0', '0', '0', '.', '.'],
		['.', '0', '0', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.']]
		
#Function for displaying a grid formatted in a list
#passedGrid is the reference to the list containing the grid
#numRows is the number of rows in the grid
#numCols is the number of columns in the grid
def grid_Display(passedGrid, numRows, numCols):
	#Line to be printed
	line = ''
	
	for r in range(numRows):
		for c in range(numCols):
			line += passedGrid[c][r]
		print(line)
		line = ''

#Testing Case
grid_Display(grid, len(grid[0]), len(grid))