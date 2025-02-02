class Solution:
    def rob(self, nums: List[int]) -> int:
    #     return self._rob(nums,len(nums)-1)
    # def _rob(self,nums,i):
    #     if i<0:
    #         return 0
    #     return max(self._rob(nums,i-1),self._rob(nums,i-2)+nums[i])
        
    #     n=len(nums)
    #     if n==0:return 0
    #     memo=[-1]*n
    #     return self._rob(nums,memo,n-1)
        
    # def _rob(self,nums,memo,i):
    #     if i<0:return 0

    #     if memo[i]>=0:
    #         return memo[i]
        
    #     memo[i]=max(self._rob(nums,memo,i-1),self._rob(nums,memo,i-2)+nums[i])
    #     return memo[i]
        # n=len(nums)
        # if n==0:return 0
        # if n==1:return nums[0]
        # memo=[-1]*n
        # memo[0],memo[1]=nums[0],max(nums[1],nums[0])
        # for i in range(2,n):
        #     memo[i]=max(memo[i-2]+nums[i],memo[i-1])
        # return memo[-1]
        

        n=len(nums)

        prev1=0
        prev2=0
        for i in range(n):
            prev1,prev2=max(prev2+nums[i],prev1),prev1
        return prev1