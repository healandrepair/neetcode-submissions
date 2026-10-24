class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxLen = len(word1) + len(word2)

        indexS = 0
        string = []
        # Use list, strings are immutable so it has to recreate the whole thing every add
        while indexS < maxLen:
            if (indexS < len(word1) and indexS < len(word2)):
                string.append(word1[indexS])
                string.append(word2[indexS])
            else:
                print(indexS)
                if (indexS > len(word1) - 1):
                    string.append(word2[indexS:])
                elif (indexS > len(word2) - 1):
                    string.append(word1[indexS:])
                
                break;
                
            indexS += 1

        return "".join(string)
        
