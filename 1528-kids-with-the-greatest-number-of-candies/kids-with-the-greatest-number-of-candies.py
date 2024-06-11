# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         a=max(candies)
#         b=[]
#         for i in range(len(candies)):
#             b.append(candies[i]+extraCandies>=a)
#         return b
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=max(candies)
        b=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies >=a:
                b.append(True)
            else:
                b.append(False)
        return b
