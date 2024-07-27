from typing import List
from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Create an adjacency list for the graph
        graph = [[] for _ in range(n)]
        for a, b in dislikes:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        # Initialize color array, -1 means uncolored
        color = [-1] * n
        
        def bfs(start):
            queue = deque([start])
            color[start] = 0  # Start coloring with color 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color
                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # Not colored
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:  # Conflict in coloring
                        return False
            return True
        
        # Try to color each component
        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False
        
        return True
