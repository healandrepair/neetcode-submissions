class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        currTurb = 0   # comparisons count
        maxTurb = 1
        prev = None

        if len(arr) == 1:
            return 1

        for R in range(1, len(arr)):
            if arr[R] == arr[R-1]:
                currTurb = 0
                prev = None
                maxTurb = max(maxTurb, 1)
                continue

            if arr[R] > arr[R-1]:
                if prev == "<" or prev is None:
                    currTurb += 1
                else:
                    currTurb = 1
                prev = ">"
            else:  # arr[R] < arr[R-1]
                if prev == ">" or prev is None:
                    currTurb += 1
                else:
                    currTurb = 1
                prev = "<"

            maxTurb = max(maxTurb, currTurb + 1)

        return maxTurb
