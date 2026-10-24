class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        newStr = ""
        for i in t:

            while j < len(s):
                print(s[j])
                if (i == s[j]):
                    print(j)
                    newStr += i
                    j += 1
                    break
                j += 1
        
        # if ()
        
        return len(t) - len(newStr)