class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in "+-*/":
                try:
                    r = stack.pop()
                    l = stack.pop()
                    if c == "+": res = l + r
                    elif c == "-": res = l - r
                    elif c == "*": res = l * r
                    elif c == "/": res = int(l / r)

                    stack.append(res)
                except:
                    continue

            else:
                stack.append(int(c))

        ans = stack.pop()
        return ans