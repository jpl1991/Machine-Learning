'''
Spiral Matrix

Given a matrix of m*n elements(m rows, n colums), return all elements
of the matrix in spiral order.

example 1:
	1,2,3
	4,5,6
	7,8,9
output: 1,2,3,6,9,8,7,4,5

example 2:
	1,2,3,4,
	5,6,7,8
	9,10,11,12
output: 1,2,3,4,8,12,11,10,9,5,6,7

'''



def spiralMatrix(matrix):
	rows = len(matrix)
	if rows <=1:
		return s.extend(matrix[0])

	cols = len(matrix[0])
	if cols == 1:
		for row in matrix:
			s.append(row[0])

	# n
	s.extend(matrix[0])    # add first row to list
	
	# (m-1)*(n-1)
	for row in matrix[1:rows-1]:
		s.append(row[cols-1])     # add right side elements to list

	# n
	s.extend(matrix[rows-1][::-1]) # add last row to list

	r = []

	# (m-1)*(n-1)
	for row in matrix[1:rows-1]:
		r.append(row[0]) 		# add left side elements to the list
	# m
	s.extend(r[::-1])

	matrix = matrix[1:rows-1]
	
	# (m-1)(n-1)
	new_matrix =  [row[1:cols-1] for row in matrix]


	# one recusive time complexity 2n + m + 3(m*n) = (m+n)+(m*n)
	# total timecomplexity ((m+n) + (m*n))^m
	spiralMatrix(new_matrix)


s = []

grid = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
grid2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16]
]

spiralMatrix(grid)

print(s)