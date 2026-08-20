class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[c] != top_element:
                    return False
            else:
                stack.append(c)

        if stack:
            return False

        return True