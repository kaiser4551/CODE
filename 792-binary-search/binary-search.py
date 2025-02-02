class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)-1
        l,r=0,n
        # mid=(l+r)/2
        while l<=r:
            mid=(r-l)//2 +l
            if(target==nums[mid]):
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1
