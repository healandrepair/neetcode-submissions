class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort()

        result = list()

        odds = list()

        
        for i in nums:
            if (i % 2 == 0):
                result.append(i)
            else:
                odds.append(i)

        return result + odds




