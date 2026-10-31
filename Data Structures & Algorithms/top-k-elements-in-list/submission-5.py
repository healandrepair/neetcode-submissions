class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        addDict = dict()


        for i in nums:
            if i not in addDict:

                addDict[i] = 1
            else:
                val = addDict[i] + 1
                addDict[i] = val

        valReturn = []
        
        sortedDict = sorted(addDict, key= lambda x: addDict[x], reverse=True)
        print(sortedDict)
        # for key,val in addDict.items():
        #     if val >= k:
        #         valReturn.append(key)

        for i in range(k):
            valReturn.append(sortedDict[i])
        
        return valReturn


            