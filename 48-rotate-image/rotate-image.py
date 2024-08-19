class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)

        top=0
        bottom=rows-1

        while top<=bottom:
            for col in range(rows):
                matrix[top][col],matrix[bottom][col]=matrix[bottom][col],matrix[top][col]
            bottom-=1
            top+=1
        
        for i in range(rows):
            for j in range(i+1,rows):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix