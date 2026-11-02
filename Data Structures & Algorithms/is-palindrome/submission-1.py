class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0

        sTrip = [i for i in s if i.isalnum()]
        j = len(sTrip) - 1
        while i < j:
            if sTrip[i].lower() != sTrip[j].lower():
                return False

            i += 1
            j -= 1
        return True