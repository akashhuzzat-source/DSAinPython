class Solution:
    def linearSearch(self, nums, target):
        found = False
        for j in range(len(nums)):
            if nums[j] == target:
                found= True
                return j
        if not found:
            return -1
            
        