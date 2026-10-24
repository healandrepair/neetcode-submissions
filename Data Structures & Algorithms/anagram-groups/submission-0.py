class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalList = []

        dictionary = dict()
        for i in strs:
            val = str(sorted(i))
            if val in dictionary:
                dictionary[val] += [i]
            else:
                dictionary[val] = [i]
        
        for x in dictionary:
            finalList.append(dictionary[x])

        return finalList
