class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curMax = -1

        for i in range(len(heights) - 1):
            for j in range(1, len(heights)):
                bucket = heights[i] if heights[i] < heights[j] else heights[j]
                width = abs(i - j)
                curMax = bucket * width if bucket * width > curMax else curMax

        return curMax