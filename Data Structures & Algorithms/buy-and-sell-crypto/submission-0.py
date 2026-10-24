class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L, R = 0, 0
        largestDiff = 0
        lowestPrice = float("inf")
        for R in range(len(prices)):
            lowestPrice = min(lowestPrice, prices[R])

            total = prices[R] - lowestPrice
            if total > largestDiff:
                largestDiff = total
        
        return largestDiff

