class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize min_price as infinity and max_profit as 0
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            # update min_price with the min between current and previous min_price
            min_price = min(min_price, price)
            # update max_profit with the max between current max_profit and the difference between current price and min_price
            max_profit = max(max_profit, price - min_price)
        return max_profit

# Time complexity: O(n) & Space complexity: O(1)