class Solution(object):
	def searchMatrix(self, matrix, target):
		'''
		:type: matrix:List[List[]]
		:type: target: int
		:rtype: bool
		'''
		rows = len(matrix)
		if(rows<1):
			return False


		cols = len(matrix[0])

		if(cols < 1):
			return False

		result = False

		count = 0

		while(count < rows):
			
			if(matrix[count][-1] >=target):

				if(matrix[count][0] <= target):

					for i in range(0, cols):
						if(matrix[count][i] == target):
							return  True
			count += 1

		return result


matrix =[[1,3,5,7],[10,11,16,20],[23,30,34,50]]

target = 6

sol = Solution()

re = sol.searchMatrix(matrix, target)

print(re)

		
		