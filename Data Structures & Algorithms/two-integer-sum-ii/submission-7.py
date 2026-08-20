class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        if len(numbers) == 0:
            return res

        for i in range(len(numbers)):
            aim = target - numbers[i]
            
            left = i + 1
            right = len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2

                if numbers[mid] == aim:
                    res.append(i + 1)
                    res.append(mid + 1)
                    return res
                
                if numbers[mid] < aim:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return res