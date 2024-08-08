# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         a=[]
#         n=len(nums)
#         def sub(i,n,nums,arr):
#             if i==0:
#                 a.append(arr.copy())
#                 return 
#             sub(i-1,n,nums,arr)
#             arr.append(nums[i-1])
            
#             sub(i-1,n,nums,arr)
#             arr.pop()
            
#         arr=[]
#         sub(n,n,nums,arr)
#         return a
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        arr=[]
        for num in range(1<<n):
            sub=[]
            for i in range(n):
                if (num &(1<<i)):
                    sub.append(nums[i])
            arr.append(sub)
        return arr
                