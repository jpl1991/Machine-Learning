''' In a NxN grid representing a field of cherries, each cell is one of three possible integers.
    * 0 means the cell is empty, so you can pass throung,
    * 1 means the cell contains a cherry, that you can pick up and pass through;
    * -1 means the cell contains a thorn that blocks your way

    Your task is to collect maximum number of cherries possible by following the rules below:

    * Starting the position(0,0) and reaching (N-1,N-1) by moving right or down through valid path cells(with value 0 or 1);
    * After reaching (N-1,N-1), returning to (0,0) by moving left or up through valid path cells;
    * When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
    * If there is no valid path between(0,0) and (N-1,N-1), then no cherries can be collected.

'''
grid = [[0,1,-1],
        [1,0,-1],
        [1,1,1]]

grid2 = [
        [0, 1, 1, 1],
        [1, 0, 1, -1],
        [1,-1,-1,-1],
        [1, 1, 1, 1]
        ]

def cherryPickUp(grid):
    L = len(grid)
    dp = [[0 for _ in range(L)] for _ in range(L)]
    dp[0][0] = grid[0][0]

    for t in range(1,2*L-1):
        for i in range(L)[::-1]:
            for p in range(L)[::-1]:
                j = t-i
                q = t -p
                if (j<0 or q <0 or j >= L or q >= L or grid[i][j] <0 or grid[p][q] < 0):
                    dp[i][p] = -1
                    continue
                if i > 0:dp[i][p] = max(dp[i][p],dp[i-1][p])
                if p > 0:dp[i][p] = max(dp[i][p],dp[i][p-1])
                if i>0 and p>0:dp[i][p] = max(dp[i][p],dp[i-1][p-1])
                if dp[i][p] >= 0:
                    second = grid[p][q] if i != p else 0
                    dp[i][p] += grid[i][j] + second
    return max(dp[-1][-1],0)

output = cherryPickUp(grid2)
print("Total pick up:", output)


#top down
def cherryPickUp3d(grid):
    N = len(grid)
    memo = [[[None]*N for _1 in range(N)] for _2 in range(N)]

    def dp(r1, c1, c2):
        r2 = r1 + c1 - c2
        if(N==r1 or N ==r2 or N == c1 or N==c2 
            or grid[r1][c1]==-1 or grid[r2][c2]==-1):

            return float('-inf')

        elif r1 == c1 == N-1:
            return grid[r1][c1]
        elif memo [r1][c1][c2] is not None:
            return memo[r1][c1][c2]
        else:
            ans = grid[r1][c1] + (c1!=c2)*grid[r2][c2]
            ans += max(dp(r1, c1+1, c2+1), 
                       dp(r1+1, c1,c2+1),
                       dp(r1, c1+1, c2),
                       dp(r1+1, c1, c2)
                       )
        memo[r1][c1][c2] = ans
        #print('r1:{} , c1:{}'.format(r1,c1))
        #print('r2:{}, c2:{}'.format(r2,c2))
        #print(memo)
        return ans
    return max(0, dp(0,0,0)), memo


grid3 = [
        [1,1,1,0,0],
        [0,0,1,0,1],
        [1,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,1,1]
]

output3, memory = cherryPickUp3d(grid3)

print(output3)
print(memory)


def cherryPickUpP(grid):
	N = len(grid)

	memory = [[[None]*N for _ in range(N)] for _ in range(N)]

	def findMax(r1, c1, r2, c2):

		if(r1 == N or c1 == N or r2 ==N or c2 == N
			or grid[r1][c1]==-1 or grid[r2][c2]==-1):
			return float('-inf')

