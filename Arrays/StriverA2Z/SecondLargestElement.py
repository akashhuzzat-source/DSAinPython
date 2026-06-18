class Solution:
    def secondLargestElement(self, nums):
        newnums=sorted(nums)
        if (newnums[0]==newnums[len(newnums)-1]):
            return -1
        elif (newnums[len(nums)-2]<newnums[len(nums)-1]):
            return newnums[len(nums)-2]
        else:
            newnums.pop(len(nums)-1)
            return self.secondLargestElement(newnums)