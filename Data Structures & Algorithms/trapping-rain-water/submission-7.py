class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        while height[left] <= 0 and left < len(height) - 1:
            left += 1
        leftmax = height[left]
        
        right = len(height) - 1
        while height[right] <= 0 and right >= 0:
            right -= 1
            if right == left:
                return 0
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