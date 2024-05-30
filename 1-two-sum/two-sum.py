# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         required = {}
#         for i in range(len(nums)):
#             if target - nums[i] in required:
#                 return [required[target - nums[i]],i]
#             else:
#                 required[nums[i]]=i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found