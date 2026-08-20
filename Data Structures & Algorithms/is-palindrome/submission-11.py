class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Lọc danh sách (List Comprehension)
        newS = [c.lower() for c in s if c.isalnum()]
        
        # Slicing để đảo ngược và so sánh
        return newS == newS[::-1]