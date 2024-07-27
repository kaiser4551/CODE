class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        row = len(mat)
        col = len(mat[0])
        dist=[[float('inf') for _ in range(col)]for _ in range(row)]

        queue = deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    dist[i][j]=0
                    queue.append((i,j))
        
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            x,y=queue.popleft()

            for dx,dy in directions:
                nx ,ny = x+dx ,y+dy
                if 0<=nx<row and 0<=ny<col:
                    if dist[nx][ny]>dist[x][y]+1:
                        dist[nx][ny]=dist[x][y]+1
                        queue.append((nx,ny))

        return dist


