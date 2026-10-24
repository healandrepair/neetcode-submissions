class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempSet = set();
        longest = 0

        j = 0
        i = 0
        while j < len(s):
            if s[j] not in tempSet:
                tempSet.add(s[j])
                j+= 1
                longest = max(longest, len(tempSet))
            else:
                while True:
                    if (s[i] == s[j]):
                        i+= 1
                        longest = max(longest, len(tempSet))
                        break
                    tempSet.remove(s[i])
                    i += 1
                    longest = max(longest, len(tempSet))
                j+= 1
                
        print(tempSet)
        
        return longest



