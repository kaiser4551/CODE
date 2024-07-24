class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent=[i for i in range(len(isConnected))]
        rank=[1]*len(isConnected)

        def find(n):
            if parent[n]==n:
                return n
            parent[n]=find(parent[n])
            return parent[n]
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)

            if p1==p2:
                return 0
            elif rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return 1

        n=len(isConnected)
        res=n
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    res-=union(i,j)
        return res