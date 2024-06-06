# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l,r=0,len(nums)-1
#         while l<=r:
#             m=l+(r-l)//2
#             if nums[m]==target:
#                 return m
#             elif nums[m]>target:
#                 if nums[r]>target:
#                     r=m-1
#                     if nums[r]==target:
#                         return r
#                 else:
#                     l=m
#                     if nums[l]==target:
#                         return l
               
#         return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
