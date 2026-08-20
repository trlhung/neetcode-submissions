class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        for i in range(0, len(nums) - 2, 1):
            a = nums[i]

            for j in range(i + 1, len(nums) - 1, 1):
                b = nums[j]

                for k in range(j + 1, len(nums), 1):
                    c = nums[k]
                
                    if a + b + c == 0:
                        if any([
                            [a, b, c] in res,
                            [a, c, b] in res,
                            [b, a, c] in res,
                            [b, c, a] in res,
                            [c, a, b] in res,
                            [c, b, a] in res
                        ]):
                            continue
                        res.append([a, b, c])
        return res