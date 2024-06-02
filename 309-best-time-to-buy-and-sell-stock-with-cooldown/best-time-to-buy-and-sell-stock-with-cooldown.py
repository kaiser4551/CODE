# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy=prices[0]
#         profit=0
#         for i in range(1,len(prices)):
#             if prices[i]<buy:
#                 buy=prices[i]
#             elif profit<prices[i]-buy:
#                 profit+=prices[i]-buy
#                 i+=1
#         return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float('-inf'), float('-inf'), 0
        
        for price in prices:
            sold, held, reset = (
                held + price,                   # Profit after selling stock held
                max(held, reset - price),       # Max of holding or buying stock
                max(sold, reset)                # Max of being in cooldown or not holding stock
            )

        return max(sold, reset)                # Max profit is either if we have just sold or are in cooldown