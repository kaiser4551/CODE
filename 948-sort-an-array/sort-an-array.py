
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, low, mid, high):
            left = arr[low:mid + 1]
            right = arr[mid + 1:high + 1]
            i = j = 0
            k = low
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        
        def ms(arr, low, high):
            if low < high:
                mid = (low + high) // 2
                ms(arr, low, mid)
                ms(arr, mid + 1, high)
                merge(arr, low, mid, high)
        
        ms(nums, 0, len(nums) - 1)
        return nums