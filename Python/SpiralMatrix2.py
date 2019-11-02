'''
Given a positive integer n, generate a square matrix filled in 
with elements from 1 to n^2 in spiral order

example:
	input: 3
	output:
		1,2,3
		8,9,4
		7,6,5
'''

class Solution(object):

	def generateMatrix(self, n):
		'''
		type n: int
		rtype: List[List[]]
		'''
		rows = cols = n

		matrix = [[0 for _ in range(n)] for _ in range(n)]

		e = 0
		for row in matrix:
			for c in row:
				c = e + 1
				e += 1 




n = 3

matrix = [[0 for _ in range(n)] for _ in range(n)]
e = 0
for row in range(n):
	for c in range(n):
		matrix[row][c] = e+1 
		e += 1

print(matrix)

