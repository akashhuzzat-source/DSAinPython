class Solution:
    def findDuplicate(self, nums):
        # Your code goes here
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    return nums[j]
                    