# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp=[[1]*n for _ in range(m)]
#         def path(x,y):
#             if x==0 and y==0 :return 1
#             if x<0 or y<0:return 0
#             if dp[x][y]!=1:
#                 return dp[x][y]
#             left=path(x-1,y)
#             up=path(x,y-1)

#             dp[x][y]=up+left
#             return dp[x][y]
#         return path(m-1,n-1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]