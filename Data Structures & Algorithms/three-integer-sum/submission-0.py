class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)

        j = 0
        finalArray = set()
        # j < i < k (need is k)
        while j < len(nums):
            seenDict = dict()
            for i in range(j+1, len(sortedNums)):
                need = 0 - sortedNums[i] - sortedNums[j]
                # Need is the values required (k)
                if need in seenDict:
                    finalArray.add((sortedNums[j], sortedNums[i], need))
                
                seenDict[sortedNums[i]] = True # value can be anything, store the i

            j += 1


        return list(finalArray)
