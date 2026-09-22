class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        front = 0
        end = len(s) - 1
        while front < end:
            if not s[front].isalnum():
                front += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue

            if s[front] != s[end]:
                return False
            front += 1
            end -= 1
        return True