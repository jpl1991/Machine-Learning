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

grid2 = [[0,1,1,1],
        [1,0,1,-1],
        [1,-1,-1,-1],
        [1,1,1,1]]

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
