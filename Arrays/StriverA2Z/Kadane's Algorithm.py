class Solution:
    def maxSubArray(self, nums):
        maximum = nums[0]
        current = 0

        for num in nums:
            current += num
            maximum = max(maximum, current)

            if current < 0:
                current = 0

        return maximum        