def minPathSum(grid):
    cols = len(grid[0])
    rows = len(grid)

    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):

            if(row==0 and col!=0):
                new_grid[row][col] =grid[row][col] + grid[row][col-1]
            if(row!=0 and col==0):
                new_grid[row][col] =grid[row][col] + grid[row-1][col]
            if(row!=0 and col!=0):
                new_grid[row][col] = grid[row][col]+ min(new_grid[row-1][col],new_grid[row][col-1])

    return new_grid

grid = [
        [1,2,3,15],
        [12,5,13,7],
        [8,9,10,11],
        [10,2,14,1]
    ]

output = minPathSum(grid)

print("Minimum:",output)