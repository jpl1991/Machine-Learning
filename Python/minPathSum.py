#top down:
def minPathSum(grid):
    cols = len(grid[0])
    rows = len(grid)

    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    new_grid[0][0] = grid[0][0]

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

#down top:
def minPathSum2(grid):
    cols = len(grid[0])
    rows = len(grid)

    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    new_grid[rows-1][cols-1] = grid[rows-1][cols-1]
    for row in range(rows-1,-1,-1):

        for col in range(cols-1,-1,-1):

            if row == rows-1 and col!=cols-1:
                new_grid[row][col] = grid[row][col] + new_grid[row][col+1]

            if col == cols-1 and row!= rows-1:
                new_grid[row][col] = grid[row][col] + new_grid[row+1][col]

            if col!=cols-1 and row!=rows-1:
                new_grid[row][col] = grid[row][col] + min(new_grid[row+1][col], new_grid[row][col+1])

    return new_grid

output2 = minPathSum2(grid)
print("down to top minimun: ", output2)



st = "kincenvizh"
setstr = set()

setstr.add("ki")
setstr.add("ki")
print(setstr)

print(len(st))
for s in range(1, len(st)):
    print(st[:s])

















