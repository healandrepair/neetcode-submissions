class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedS = []

        hashmap = dict()

        for s in strs:
            sSorted = "".join(sorted(s))
            if (sSorted not in hashmap):

                hashmap[sSorted] = [s]
            else:
                countActualValues = hashmap[sSorted]
                countActualValues.append(s)
                hashmap[sSorted] = countActualValues

    
        
        return list(hashmap.values())