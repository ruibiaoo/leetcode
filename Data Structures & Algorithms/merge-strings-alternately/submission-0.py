class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = min(len(word1), len(word2)) -1
        ans = ""

        while left <= right:
            ans += word1[left]
            ans += word2[left]
            left += 1
        
        if len(word2) > len(word1):
            ans += word2[right+1:]
        else:
            ans += word1[right+1:]
        
        return ans
        