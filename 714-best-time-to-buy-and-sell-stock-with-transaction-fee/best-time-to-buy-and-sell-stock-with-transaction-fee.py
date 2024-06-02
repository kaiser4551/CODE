class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy=prices[0]
        profit=0
        for p in prices[1:]:
            if p<buy:
                buy=p
            elif p-buy>fee:
                profit+=p - buy -fee
                buy=p-fee
        return profit

# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         buy = float('-inf')
#         sell = 0

#         for price in prices:
#             buy = max(buy, sell - price)
#             sell = max(sell, buy + price - fee)

#         return sell