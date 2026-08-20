class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        left = 0
        leftmax = height[left]
        right = len(height) - 1
        rightmax = height[right]
        res = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                leftmax = height[left] if height[left] > leftmax else leftmax
                res += leftmax - height[left]
                continue
            
            right -= 1
            rightmax = height[right] if height[right] > rightmax else rightmax
            res += rightmax - height[right]

        return res