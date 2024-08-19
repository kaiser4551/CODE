class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr=[]
        arr2=[]
        for i in range(len(nums)):
            if nums[i]<0:
                arr.append(nums[i])
            else:
                arr2.append(nums[i])
        arr3=[]
        for i in range(len(arr2)):
            arr3.append(arr2[i])
            arr3.append(arr[i])
        return arr3