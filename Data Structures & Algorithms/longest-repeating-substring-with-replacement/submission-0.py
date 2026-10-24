class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        charFreq = dict()

        L = 0
        for R in range(len(s)):
            if s[R] in charFreq:
                charFreq[s[R]] += 1
            else:
                charFreq[s[R]] = 1
            
            # R - L + 1 is lengthOfCurrentWindow
            while R - L + 1 - max(charFreq.values()) > k:
                # Case when you need to shift (shrink)the left pointer
                charFreq[s[L]] -= 1
                L += 1
                
            result = max(result, R - L + 1)
        
            
                    
        return result




                

                  
