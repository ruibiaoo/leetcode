class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = sorted(nums)

        for i in range (0, len(nums)- 3):
            if i > 0  and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums) -2):
                if nums[j] == nums[j-1] and j> i+1:
                    continue
                left = j+1
                right = len(nums) - 1

                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left +=1
                        right -=1
                    
                        while nums[left] == nums[left-1] and left < right:
                            left += 1
                        
                        while nums[right] == nums[right+1] and left < right:
                            right -=1

        return ans
            

        