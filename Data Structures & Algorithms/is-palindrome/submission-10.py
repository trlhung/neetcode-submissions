class Solution:
    def checkChar(self, c1: str, c2: str) -> bool:
            if c1.lower() == c2.lower():
                return True
            return False

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        head = 0
        tail = len(s) - 1

        while head != tail and head < tail:
            while not s[head].isalnum() and head < tail:
                head += 1
            while not s[tail].isalnum() and tail > head:
                tail -= 1
            
            if self.checkChar(s[head], s[tail]):
                head += 1
                tail -= 1
                continue
            else:
                return False
            
        return True

