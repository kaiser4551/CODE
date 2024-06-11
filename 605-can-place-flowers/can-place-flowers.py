# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         count=0
#         count1=0
#         for i in flowerbed:
#             if i==0:
#                 count+=1
#             elif i==1:
#                 count1+=1
#         if count >= 2*n+1 and count2<:
#             return True
#         else:
#             return False
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                # Check if the previous and next spots are also empty or if we are at the boundaries
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                    # Skip the next spot since we just planted a flower here
                    i += 1
            if count >= n:
                return True
            i += 1
        return count >= n