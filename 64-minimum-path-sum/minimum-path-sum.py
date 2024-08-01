# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m=len(grid)
#         n=len(grid[0])
#         def path(x,y):
#             if x==0 and y==0:
#                 return grid[0][0]
#             if x<0 or y<0:
#                 return float('inf')
            
#             return min(path(x-1,y),path(x,y-1))+grid[x][y]
#         return path(m-1,n-1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        dp=[[-1]*n for _ in range(m)]

        def path(x,y):
            if x==0 and y==0:
                return grid[0][0]
            if x<0 or y<0:
                return float('inf')
            if dp[x][y]!=-1:
                return dp[x][y]
            dp[x][y]=min(path(x-1,y),path(x,y-1))+grid[x][y]
            return dp[x][y]
        return path(m-1,n-1)