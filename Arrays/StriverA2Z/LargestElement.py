class Solution:
    def largestElement(self, nums):
        maximum=0
        for i in range(len(nums)):
            if (nums[maximum]<nums[i]):
                maximum=i
        return nums[maximum]