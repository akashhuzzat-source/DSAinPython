class Solution:
    def unionArray(self, nums1, nums2):
        nums3=[]
        for i in range(len(nums1)):
            nums3.append(nums1[i])
        for j in range(len(nums2)):
            nums3.append(nums2[j])
        nums3=sorted(set(nums3))
        return list(nums3)