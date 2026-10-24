class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = dict()
        for i in nums:
            print(i)
            if i in dictionary:
                return True
            else:
                dictionary[i] = 1
        
        return False
        