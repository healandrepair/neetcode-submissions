class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        globalMax = nums[0]

        currMin = 0
        globalMin = nums[0]

        total = 0
        for num in nums:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)
        
            total += num
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
        
        #  The calculation total- global min:
# i like to imagine it like an obstacle,
# if a maximum sum subarray exists in a circular formation, 
# i.e. the left and right ends of the array, then
#  the obstacle in the middle will be the minimum sum subarray, 
# so taking the total – global min, we get the circular portion which is the globalmax        
        return max(globalMax, total - globalMin) if (globalMax > 0) else globalMax


            
            
