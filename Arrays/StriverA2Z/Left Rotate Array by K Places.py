class Solution:
    def rotateArray(self, nums, k: int) -> None:
        if (k==0):
            return
        j=0
        first=nums[0]
        for i in range(len(nums)):
            if (i>=0 and i<(len(nums)-1)):
                nums[j]=nums[i+1]
                j+=1
            else:
                nums[i]=first
        return self.rotateArray(nums, k-1)

