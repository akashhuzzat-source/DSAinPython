class Solution:
    def rotateArrayByOne(self, nums):
        newnums=[]
        for i in range(len(nums)-1):
            newnums.append(nums[i+1])
        newnums.append(nums[0])
        return newnums
    