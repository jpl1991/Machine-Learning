class Solution(object):
    def __init__(self):
        self.s = []
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        print('cols:',cols)
        if (cols ==0):
            print('return none')
            return self.s
        if cols == 1:
            for row in matrix:
                self.s.append(row[0])
            return self.s

        print('rows:',rows)
        if rows <= 1:
            #print(self.s)
            result =  self.s.extend(matrix[0])
            print(result)
            return result



        self.s.extend(matrix[0])
        print(self.s)
        for row in matrix[1:rows-1]:

            self.s.append(row[cols-1])
            
        self.s.extend(matrix[rows-1][::-1])
        
        r = []
        
        for row in matrix[1:rows-1]:
            r.append(row[0])
        
        self.s.extend(r[::-1])
        
        matrix = matrix[1:rows-1]
        
        new_matrix = [row[1:cols-1] for row in matrix]
        print('new_matrix:',new_matrix)
        #print(self.s)
        self.spiralOrder(new_matrix)
        return self.s

        
grid = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

grid2 = [[7],[9],[6]]

grid3 = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]

result  = Solution()

print(result.spiralOrder(grid3))
