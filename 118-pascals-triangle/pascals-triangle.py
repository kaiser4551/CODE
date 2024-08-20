class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        
        prevrows=self.generate(numRows-1)
        newrow=[1]*numRows

        for i in range(1,numRows-1):
            newrow[i]=prevrows[-1][i-1]+prevrows[-1][i]
        prevrows.append(newrow)
        return prevrows

