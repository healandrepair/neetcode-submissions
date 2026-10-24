class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dictionary = dict()

        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1

        index = 0
        if len(dictionary) == 1:
            pass

        else:
            for i in range(len(dictionary)):

                tempVal = dictionary[i]
                while tempVal > 0:
                    nums[index] = i
                    tempVal -= 1
                    index += 1
        

