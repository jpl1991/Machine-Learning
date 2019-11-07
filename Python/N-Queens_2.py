
def totalQueens(n):

	grid = [[0 for i  in range(n)] for j in range(n)]

	storedGrid = []

	for i in range(0, n):


		for j in range (0, n):
			
