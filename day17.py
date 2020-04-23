grid = [[11110],[11010],[11000],[00100],[00011]]
from functools import lru_cache
if not grid:
    return 0
count = 0
n, m = len(grid), len(grid[0])
def dfs(i, j):
    if 0 <= i < n and 0 <= j < m:
        if grid[i][j] == '1':
            grid[i][j] = '#'
            for nr, nc in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                dfs(nr, nc)
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1':
            count += 1
            dfs(i, j)
return count