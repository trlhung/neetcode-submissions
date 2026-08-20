class Solution:
    def isValid(self, s: str) -> bool:
        oBracket = ("(", "[", "{")
        cBracket = (")", "]", "}")

        relative = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for c in s:
            if c in oBracket:
                stack.append(c)

            if c in cBracket:
                if not stack:
                    return False
                
                r = relative[c]
                if oBracket.index(r) == oBracket.index(stack[-1]):
                    stack.pop()
                    continue
                else:
                    return False

        if stack:
            return False
            
        return True