class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            
            elif s[left] != s[right]:
                ans = checkPalindrome(left, right - 1)
                res = checkPalindrome(left + 1, right)

                if ans or res == True:
                    return True
                else:
                    return False
        return True