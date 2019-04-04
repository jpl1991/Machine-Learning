def calculateProfit(n, earning, cost, e):
	money = 0
	for i in range(n):
		if(i==n-1):
			money += e*earning[i]
			return money
		if(earning[i]>cost[i]):
			money += e*earning[i]
			money = money-e*cost[i]
	return money

n , earning, cost, e = 4, [1,8,6,7],[1,3,4,1], 5

money = calculateProfit(n, earning, cost,e)

print(money)

def uniquePathsWithObstacles(obstacleGrid) -> int:
        rows  = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        tablepath = [[0 for i in range(cols)] for j in range(rows)]
        print("rows:", rows)
        for row in range(0, rows):
        	
            for col in range (0, cols):
            	
                if(col==cols-1 and row+1<rows):
                    if(tablepath[row+1][col]==0):
                        tablepath[row+1][col] = tablepath[row][col]
                    else:
                        tablepath[row+1][col] = max(tablepath[row][col],tablepath[row+1][col] )
                if(row == row-1 and col+1<cols):
                    if(tablepath[row][col+1]==0):
                        tablepath[row][col+1] = tablepath[row][col]
                    else:
                        tablepath[row][col+1] = max(tablepath[row][col],tablepath[row][col+1] )
                if(col+1<cols and row+1<row):
                    if(obstacleGrid[row][col+1]==0 and obstacleGrid[row+1][col]==0):
                        if(tablepath[row][col+1]==0):
                            tablepath[row][col+1] = obstacleGrid[row][col]+2
                        else:
                            tablepath[row][col+1] = max(obstacleGrid[row][col]+2, tablepath[row][col+1])
                        if( tablepath[row+1][col] ==0):
                            tablepath[row+1][col] = obstacleGrid[row][col]+2
                        else:
                            tablepath[row+1][col] = max(obstacleGrid[row][col]+2, tablepath[row+1][col])
        print(tablepath)
        return tablepath[rows-1][cols-1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]];

paths = uniquePathsWithObstacles(obstacleGrid)
print("paths:", paths)