class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        newnums=[]
        newnums.append(nums[0])
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                newnums.append(nums[i+1])
        return len(newnums)


