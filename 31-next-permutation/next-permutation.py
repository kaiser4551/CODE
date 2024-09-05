class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)

        if n in [0,1]:
            return
        
        largest_from_back=-1
        for i in range(n-1,-1,-1):
            if nums[i]< nums[largest_from_back]:
                for j in range(n-1,i,-1):
                    if nums[j]>nums[i]:
                        nums[i],nums[j]=nums[j],nums[i]
                        nums[i+1:]=sorted(nums[i+1:])
                        return
            else:
                largest_from_back=i
        nums.sort()