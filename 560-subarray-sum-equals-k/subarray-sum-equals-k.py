class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0
        sum_freq = {0: 1}  # Initialize with 0 sum having one occurrence
        
        for num in nums:
            cum_sum += num
            if cum_sum - k in sum_freq:
                count += sum_freq[cum_sum - k]
            sum_freq[cum_sum] = sum_freq.get(cum_sum, 0) + 1
        
        return count

