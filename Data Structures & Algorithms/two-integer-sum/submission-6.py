class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = dict()

        for i in range(len(nums)):
            compliment = target - nums[i]

            if (compliment in dictionary):
                return [dictionary[compliment], i]
            dictionary[nums[i]] = i

        return []
