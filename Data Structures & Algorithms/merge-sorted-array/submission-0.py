class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = len(nums1) -1

        for i in range(len(nums2)-1, -1, -1):
            while nums1[left] > nums2[i] and left >= 0:
                nums1[right] = nums1[left]
                left -= 1
                right -= 1
            nums1[right] = nums2[i]
            right -= 1
            
        return nums1






