class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        minLength = float("inf")
        currSum = 0 
        while j < len(nums):
            currSum += nums[j]
            
            while currSum >= target:
                print(currSum)
                print(f"abs = {i-j+1}")
                if (minLength > len(nums[i:j+1])):
                    minLength = len(nums[i:j+1])
                currSum -= nums[i]
                i += 1
            j += 1
            
        if minLength == float("inf"):
            return 0
        return minLength




        