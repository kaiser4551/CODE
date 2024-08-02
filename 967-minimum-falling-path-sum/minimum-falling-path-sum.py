class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        # Start from the second last row and move upwards
        for i in range(m - 2, -1, -1):
            for j in range(n):
                # Choose the minimum from the possible cells in the row below
                if j == 0:
                    matrix[i][j] += min(matrix[i + 1][j], matrix[i + 1][j + 1])
                elif j == n - 1:
                    matrix[i][j] += min(matrix[i + 1][j], matrix[i + 1][j - 1])
                else:
                    matrix[i][j] += min(matrix[i + 1][j], matrix[i + 1][j - 1], matrix[i + 1][j + 1])
        
        # The minimum path sum will be the minimum value in the top row
        return min(matrix[0])

        