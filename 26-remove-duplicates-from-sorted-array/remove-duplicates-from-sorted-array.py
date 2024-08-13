class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        arr = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                arr.append(nums[i])
        
        for i in range(len(arr)):
            nums[i] = arr[i]
        
        return len(arr)
