class Solution:
    def leaders(self, nums):
        leaders = []

        for i in range(len(nums)):
            isLeader = True

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    isLeader = False
                    break

            if isLeader:
                leaders.append(nums[i])

        return leaders
        