class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_min = prices[0]

        for price in prices:
            profit = max(price - curr_min, profit)
            curr_min = min(price, curr_min)
        return profit

        # [10,1,5,6,7, 0, 18]

        # profit = 0
        # for i in range(len(prices)): # O(n^2)
        #     for j in range(i+1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])
        # return profit

        