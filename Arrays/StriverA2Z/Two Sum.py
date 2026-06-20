class Solution:
    def twoSum(self, nums, target):
        newnums=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    newnums.append(i)
                    newnums.append(j)
        return newnums
        