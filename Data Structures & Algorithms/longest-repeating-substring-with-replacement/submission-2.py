class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        seen = {}

        right = 0
        left = 0

        while right < len(s):
            seen[s[right]] = 1 + seen.get(s[right], 0)
            replaced = right - left - max(seen.values()) + 1

            while replaced > k and left < right:
                seen[s[left]] = seen.get(s[left], 1) - 1
                left += 1
                
                replaced = right - left - max(seen.values()) + 1

            right += 1
            res = max(res, right - left)

        return res