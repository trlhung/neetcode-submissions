class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(nums)

        longest = 1
        curlen = 1
    
        for i in range(len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] - nums[i - 1] == 1:
                    curlen += 1
                    continue
                longest = max(longest, curlen)
                curlen = 1

            if nums[i] == nums[i - 1]:
                continue

        return max(longest, curlen)
        