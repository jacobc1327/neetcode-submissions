class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        left = 0
        for right in range(len(prices)):
            if prices[right] > prices[left]:
                maxprofit = max(maxprofit, prices[right] - prices[left])
            else:
                left = right
        return maxprofit