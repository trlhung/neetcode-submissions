class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ''
        for i in strs:
            length = len(i)
            newStr += str(length) + '#'
            for ch in i:
                newStr += ch
        return newStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            strLength = int(s[i:j])

            newStr = ''
            for p in range(j + 1, j + 1 + strLength, 1):
                newStr += s[p]
            
            res.append(newStr)
            i = j + 1 + strLength

        return res