class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        curMax = 0

        while left < right:
            height = heights[left] if heights[left] < heights[right] else heights[right]
            width = right - left
            curMax = curMax if curMax > height * width else height * width

            if heights[left] < heights[right]:
                left += 1
                
            else:
                right -= 1
    
        return curMax

