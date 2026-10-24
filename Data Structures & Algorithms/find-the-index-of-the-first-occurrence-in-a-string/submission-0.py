class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0;

        for i in range(len(needle)-1, len(haystack)):
            print(i)
            tempVal = haystack[j:i+1]
            print(f"tempval: {tempVal}")
            if tempVal == needle:
                return j
            
            j+= 1
        
        return -1


            