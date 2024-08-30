# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         dic={}
#         for num in nums:
#             if num in dic:
#                 dic[num]+=1
#             else:
#                 dic[num]=1
#         n=len(nums)
#         for num in dic:
#             if dic[num]>n/2:
#                 return num
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
