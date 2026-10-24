class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        tempSet = dict()
        for c in s:
            if c in tempSet:
                tempSet[c] += 1
            else:
                tempSet[c] = 1
            
        slen = len(s)
        j = 0

        stringC = ""
        for c in s:
            while j < len(t):
                if t[j] == c:
                    stringC += c
                    j += 1
                    break

                j += 1

        if stringC == s:
            return True
        return False