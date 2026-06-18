class Solution:
    def isSorted(self, nums):
        #your code goes here
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                return False
            
        return True