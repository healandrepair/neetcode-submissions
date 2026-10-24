class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calculateArea(height, length):
            return height * length

        currMaxArea = 0

        j = len(heights) - 1
        i = 0
        while i < j:
            print(f"j:{j}, i:{i}")
            currHeight = min(heights[j], heights[i])
            currLength = abs(j-i)
            calcArea = calculateArea(currHeight, currLength)

            if (currMaxArea < calcArea):
                print(f"jval:{heights[j]}, ival:{heights[i]}")
                print(f"{calcArea}")
                currMaxArea = calcArea
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1

        return currMaxArea



            
