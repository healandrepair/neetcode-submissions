class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        j = 0
        i = 0
        g.sort()
        s.sort()
        counter = 0
        print(g)
        print(s)
        while True:
            if (i >= len(g)):
                break
            if (j >= len(s)):
                break
            while j < len(s) and i < len(g) and s[j] >= g[i]:
                counter += 1
                i += 1
                j += 1
            while j < len(s) and i < len(g) and s[j] < g[i]:
                j += 1
                

        return counter