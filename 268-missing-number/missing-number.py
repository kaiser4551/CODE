class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()  # Sort the list first
        for i in range(len(nums)):
            if nums[i] != i:
                return i  # Return the first missing number
        # If no numbers are missing within the loop, the missing number is len(nums)
        return len(nums)
