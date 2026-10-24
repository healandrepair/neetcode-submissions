class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        firstWord = strs[0]
        longest = len(firstWord)
        for word in strs[1:]:
            i = 0

            while i < len(word) and i < len(firstWord) and word[i] == firstWord[i]:
                i += 1

            longest = min(longest, i)
        return firstWord[:longest]
