class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        left = 0
        right = len(text)-1
        while left < right:
            if not text[left].isalnum():
                left += 1
                continue
            if not text[right].isalnum():
                right -= 1
                continue
            if text[left] == text[right]:
                left += 1
                right -= 1
            else:
                return False
        return True