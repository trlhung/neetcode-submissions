class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minValue = prices[0]

        for i in prices:
            if i < minValue:
                minValue = i
            
            res = i - minValue if i - minValue > res else res
        
        return res