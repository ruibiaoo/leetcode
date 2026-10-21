class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for i in range(len(nums)):
            value = nums[i]
            complement = target - value
            
            if complement not in dict1:
                dict1[value] = i
            else:
                ans = [i, dict1.get(complement)]
                return sorted(ans)