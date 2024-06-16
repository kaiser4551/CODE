# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         insert_pos = 0
#         n=[]
#         for i in range(0,len(nums)-1):
#             if nums[i]!=0:
#                 nums[insert_pos]=n[i]
#                 insert_pos+=1
#         for i in range(0,len(nums)-1):
#             if nums[i]==0:
#                 nums[insert_pos]=n[i]
#                 insert_pos+=1
#         nums=n
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize a pointer for the position to insert the next non-zero element.
        insert_pos = 0
        
        # First pass: Move all non-zero elements to the beginning of the list.
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        # Second pass: Fill the remaining positions with zeroes.
        for i in range(insert_pos, len(nums)):
            nums[i] = 0