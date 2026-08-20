class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        seen = set()

        for i in prices:
            if len(seen) == 0:
                seen.add(i)
                continue
            
            res = res if res > (i - min(seen)) else i - min(seen)
            seen.add(i)
        
        return res if res > 0 else 0