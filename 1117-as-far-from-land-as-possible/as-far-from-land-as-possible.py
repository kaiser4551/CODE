# class Solution:
#     def maxDistance(self, grid: List[List[int]]) -> int:
#         if not grid:
#             return -1
        
#         row=len(grid)
#         col=len(grid[0])
        
#         dist=[[float('inf')for _ in range(col)]for _ in range(row)]
#         queue=deque()
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j]==1:
#                     dist[i][j]=0
#                     queue.append((i,j))
#         if not queue:
#             return -1
#         directions=[(1,0),(-1,0),(0,1),(0,-1)]

#         while queue:
#             x,y=queue.popleft()

#             for dx,dy in  directions:
#                 nx,ny=x+dx,y+dy
#                 if 0<=nx<row and 0<=ny<col:
#                     if dist[nx][ny]>dist[x][y]+1:
#                         dist[nx][ny]=dist[x][y]+1
#                         queue.append((nx,ny))
#         a=float('-inf')
#         for i in range(row):
#             for j in range(col):
#                 a=max(a,dist[i][j])
#         if a==float('inf'):
#             return -1
#         else:
#             return a

# from typing import List
# from collections import deque

from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        row = len(grid)
        col = len(grid[0])
        
        dist = [[float('inf') for _ in range(col)] for _ in range(row)]
        queue = deque()
        has_water = False
        
        # Initialize queue with all land cells and their distances
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    queue.append((i, j))
                else:
                    has_water = True
        
        if not has_water:
            return -1
        
        if not queue:
            return -1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Perform BFS to update distances
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col:  # Check bounds
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
        
        # Find the maximum distance
        max_distance = float('-inf')
        for i in range(row):
            for j in range(col):
                if dist[i][j] != float('inf'):
                    max_distance = max(max_distance, dist[i][j])
        
        return max_distance if max_distance != float('-inf') else -1
