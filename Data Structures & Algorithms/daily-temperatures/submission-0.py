class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        j = 0
        while j < len(temperatures):
            for i in range(j+1, len(temperatures)):
                if (temperatures[i] > temperatures[j]):
                    diff = i - j
                    result[j] = diff
                    break
            j += 1
        
        return result