class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        leftmax = height[left]
        rightmax = height[right]
        ans = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    ans += leftmax - height[left]
            else:
                right -= 1
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    ans += rightmax - height[right]
        return ans
        