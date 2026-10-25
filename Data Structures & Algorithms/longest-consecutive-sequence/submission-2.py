class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        streak = 0
        seen = set(nums)
        
        for num in nums:
            if num - 1 not in seen:
                length = 1

                while (num + length) in seen:
                    length += 1

                streak = max(streak, length)
        return streak

            

            