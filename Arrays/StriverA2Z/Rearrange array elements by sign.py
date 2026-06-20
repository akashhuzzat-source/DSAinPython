class Solution:
    def rearrangeArray(self, nums):
        positive=[]
        negative=[]
        final=[]
        for i in range(len(nums)):
            if(nums[i]<0):
                negative.append(nums[i])
            else:
                positive.append(nums[i])
        for j in range(len(nums)):
            if(j==0 or j%2==0):
                    final.append(positive[j//2])
            else:
                    final.append(negative[j//2])
        return final

        