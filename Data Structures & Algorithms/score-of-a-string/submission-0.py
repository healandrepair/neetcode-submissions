class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        i = 0
        for j in range(1, len(s)):
            diff = abs(ord(s[i]) - ord(s[j]))

            score += diff
            i += 1

        return score
        