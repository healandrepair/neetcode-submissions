class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = dict()
        
        for i in range(len(nums)):
            if (target - nums[i] in dictionary):
                if (dictionary[target - nums[i]] == i):
                    continue
                return [dictionary[target - nums[i]], i]      
            if nums[i] not in dictionary:
                dictionary[nums[i]] = i 


        return []
        