class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        rows=len(matrix)
        cols=len(matrix[0])
        arr=[]
        
        top , bottom = 0 , rows-1
        left , right = 0, cols-1

        while left<=right and top<=bottom:
            for j in range(left,right+1):
                arr.append(matrix[top][j])
            top+=1
            for j in range(top,bottom+1):
                arr.append(matrix[j][right])
            right-=1
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for j in range(right, left - 1, -1):
                    arr.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top along the left column
                for j in range(bottom, top - 1, -1):
                    arr.append(matrix[j][left])
                left+=1
        return arr