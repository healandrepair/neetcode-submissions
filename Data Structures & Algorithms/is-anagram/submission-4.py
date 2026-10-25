class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = dict()

        
        sSort = sorted(s)
        tSort = sorted(t)


        return sSort == tSort