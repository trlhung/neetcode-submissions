class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        height = heights[left] if heights[left] < heights[right] else heights[right]
        width = right - left

        curMax = height * width

        while left < right:
            if heights[left] < heights[right]:
                left += 1
                height = heights[left] if heights[left] < heights[right] else heights[right]
                width = right - left
                curMax = curMax if curMax > height * width else height * width
            else:
                right -= 1
                height = heights[left] if heights[left] < heights[right] else heights[right]
                width = right - left
                curMax = curMax if curMax > height * width else height * width
        
        return curMax

