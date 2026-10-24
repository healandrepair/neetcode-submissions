class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # maxNow = 0;
        # maxGreed = max(g)
        # for i in s:
        #     if (maxNow < i):
        #         if (i > maxGreed):
        #             break
        #         else:
        #             maxNow = max(i, maxNow)


        # return maxNow
        # counter = 0 
        # sortedG = sorted(g)

        # for i in g:
        #     if (i in s):
        #         counter += 1

        sortedG = g.sort()
        sortedS = s.sort()
        counter = 0
        j = 0
        i = 0

        while i < len(g) and j < len(s):
            print("i " + str(i))
            print("j " + str(j))
            if (s[j] >= g[i]):
                counter += 1
                j += 1
                i += 1
            else:
                j += 1

            
            
        
        
        return counter

            


                

            

