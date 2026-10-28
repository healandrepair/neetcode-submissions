class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS = [i for i in s if i.isalpha() or i.isnumeric()]
        j = len(newS) - 1
        print(newS)
        for i in range(len(newS)):
            print(i)
            print(j)
            if (j < 0):
                break
            if (newS[j].lower() == newS[i].lower()):
                j -= 1
                continue
            else:
                return False
            
        return True
        