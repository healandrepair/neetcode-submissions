class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setNums1 = set(nums1)
        setNums2 = set(nums2)

        finalSet = set()
        for j in setNums1:
            if j in setNums2:
                finalSet.add(j)

        return list(finalSet)
        