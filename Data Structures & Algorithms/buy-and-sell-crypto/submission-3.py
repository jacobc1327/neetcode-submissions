class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxprofit = 0
        for right in range(len(prices)):
            if prices[right]>prices[left]:
                maxprofit = max(maxprofit, prices[right]-prices[left])
            else:
                left=right
        return maxprofit