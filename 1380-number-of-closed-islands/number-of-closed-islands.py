class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r==rows or c==cols or grid[r][c]!=0:
                return 
            grid[r][c]=2
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0 and (r in[0,rows-1] or c in[0,cols-1]):
                    dfs(r,c)
        closed_islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    dfs(r,c)
                    closed_islands+=1
        return closed_islands