class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def swap(start, end):
            tempEnd = end - 1 

            while start < tempEnd:
                s[start], s[tempEnd] = s[tempEnd], s[start]
                start += 1
                tempEnd -= 1

            # print(f"range {start},{tempEnd // 2}")
            # for i in range(start, end // 2):
            #     print(f"{i},{tempEnd},")
            #     print(f"{s[i]},{s[tempEnd]},")
            #     s[i], s[tempEnd] = s[tempEnd], s[i]
            #     tempEnd -= 1
            # print("Exit swap")

        j = len(s) - 1

        for i in range(len(s) // 2):
            s[i], s[j] = s[j], s[i]
            j -= 1

        #  second pass through
        y = 0
        justSwapped = False
        print("HI")
        for x in range(len(s)):
            if (x + 1 == len(s)):
                print("pp")
                print(x)
                x = x + 1
                pass
            elif (s[x] != " "):
                if (justSwapped == True):
                    y = x
                    justSwapped == False
                continue
            
            print("SWAP")
            print(f"SWAP {y}, {x-1}")
            swap(y, x)
            y = x + 1

        print(s)
