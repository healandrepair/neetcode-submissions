class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = dict()

        for i, val in enumerate(nums):
            complement = target - val

            if complement in dictionary:
                return [dictionary[complement], i]

                
            dictionary[val] = i

        
        return []
        