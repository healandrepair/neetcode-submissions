class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxLen = len(word1) + len(word2)

        indexS = 0
        string = ""
        while indexS < maxLen:
            if (indexS < len(word1) and indexS < len(word2)):
                string += word1[indexS]
                string += word2[indexS]
            else:
                print(indexS)
                if (indexS > len(word1) - 1):
                    string += word2[indexS:]
                elif (indexS > len(word2) - 1):
                    string += word1[indexS:]
                
                break;
                
            indexS += 1

        return string
        
