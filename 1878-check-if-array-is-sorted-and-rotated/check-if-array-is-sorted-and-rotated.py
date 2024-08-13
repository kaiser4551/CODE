class Solution:
    def check(self, nums: List[int]) -> bool:
        op=0
        l=len(nums)
        for i in range(l):
            if nums[(i+1)%l]>=nums[i]:
                pass
            else:
                op+=1
                if op>1:
                    return False
        return True
            
            