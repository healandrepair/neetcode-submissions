class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) -1
        res = False
        while i < j:
            if (s[j] != s[i]):
                skipj = s[i:j]
                skipi = s[i+1:j+1]
                return skipj == skipj[::-1] or skipi == skipi[::-1]
            
            i += 1
            j -= 1
            
        return True