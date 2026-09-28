class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        def isAlphaNumeric(char: str) -> bool:
            if (
                (ord('a') <= ord(char) <= ord('z')) or
                (ord('0') <= ord(char) <= ord('9'))
            ):
                return True
            return False

        while left < right:
            while (left < right) and (not isAlphaNumeric(s[left])):
                left += 1
            while (left < right) and (not isAlphaNumeric(s[right])):
                right -= 1
            # print(f'{(left, right)}: {(s[left], s[right])}')
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
            


# 'hell lleh' odd length are still palindrome
# '' left is 0 right -1  left < right False! return True
# 'a' left is 0 right is 0 left < right False return True