class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = dict()

        for i in nums:
            if i in dictionary:
                val = dictionary[i]
                dictionary[i] = val + 1
            else:
                dictionary[i] = 1
        print(dictionary)

        for x in dictionary:
            val = dictionary[x]
            if val > 1:
                return True
        return False