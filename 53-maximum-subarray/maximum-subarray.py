class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=0
        s=0
        for i in nums:
            s=s+i
            if s <=0:
                s=0
            else:
                maxi=max(maxi,s)

        if maxi==0:
            maxi = -99999999
            for i in nums:
                maxi=max(maxi,i)
            

        return(maxi)