
def sortMatrix(matrix):
	row_len = len(matrix)
	col_len = len(matrix[0])

	#temp = [0]*(row_len*col_len)
	temp = []
	for rows in matrix:
		for col in rows:
			temp.append(col)

	temp.sort()
	k = 0
	for i in range(0, row_len):
		for j in range(0, col_len):
			matrix[i][j] = temp[k]
			k+=1

	return matrix

matrix = [[ 5, 12, 17, 21, 23],
 [ 1,  2,  4,  6,  8],
 [12, 14, 18, 19, 27],
 [ 3,  7,  9, 15, 25]]

sorted_matrix = sortMatrix(matrix)

print(sorted_matrix)