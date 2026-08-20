class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = []
        for i in s:
            if not i.isalnum():
                continue
            
            newS.append(i)
        
        for i in range(len(newS)):
            if newS[i].lower() == newS[len(newS) - i - 1].lower():
                continue
            return False
        
        return True