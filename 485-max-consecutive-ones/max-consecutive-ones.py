class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        cnt=0
        maxcnt=0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
                maxcnt=max(cnt,maxcnt)
            else:
                cnt=0

        return maxcnt