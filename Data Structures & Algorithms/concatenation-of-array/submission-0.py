class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = []
        i = 0
        while i < 2:
            for element in nums:
                nums2.append(element)

            i += 1
        return nums2

        