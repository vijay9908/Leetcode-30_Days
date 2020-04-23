class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        new_grid = [[0]*C for _ in range(R)]
        new_grid[0][0] = grid[0][0]
        for c in range(1, C):
            new_grid[0][c] = new_grid[0][c-1] + grid[0][c]
        for r in range(1, R):
            new_grid[r][0] = new_grid[r-1][0] + grid[r][0]
        
        for r in range(1,R):
            for c in range(1,C):
                
                new_grid[r][c] = min(grid[r][c]+new_grid[r-1][c], grid[r][c]+new_grid[r][c-1])
        
        return new_grid[R-1][C-1]
            
                    
        