class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        max_profit = 0

        for value in prices:
            if value < min_price:
                min_price = value
            current_profit= value - min_price
            max_profit = max(max_profit, current_profit)
        return max_profit