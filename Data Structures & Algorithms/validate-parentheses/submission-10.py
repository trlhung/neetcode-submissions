class Solution:
    def isValid(self, s: str) -> bool:
        # remaining = (')', ']', '}')

        oBracket = ['(', '[', '{']

        cBracket = [')', ']', '}']

        remaining = [0, 0, 0]



        stack = []

        last = -1



        for c in s:

            if c in oBracket:

                stack.append(c)

                remaining[oBracket.index(c)] += 1

                last = oBracket.index(c)



            if c in cBracket:

                if not stack or remaining[cBracket.index(c)] <= 0 or cBracket.index(c) != last:

                    return False

               

                remaining[cBracket.index(c)] -= 1

                stack.pop()

                last = oBracket.index(stack[-1]) if stack else -1



        if stack:

            return False

       

        return True 

