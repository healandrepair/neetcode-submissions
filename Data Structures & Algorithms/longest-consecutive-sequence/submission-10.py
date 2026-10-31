class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        print(sortedNums)
        # Sliding window
        i = 0
        j = 0
        longest = 0
        seq = set();
        if (len(sortedNums) > 0):
            seq.add(sortedNums[i])
            longest = 1

        while i < len(sortedNums) and j < len(sortedNums):
            if (sortedNums[j] not in seq):
                if (j - 1 >= 0 and sortedNums[j-1] == sortedNums[j] - 1):
                    seq.add(sortedNums[j])
                    longest = max(longest, len(seq))
                else:
                    i = j
                    seq = set()
                    seq.add(sortedNums[j])
            j += 1
            # print(seq)

            
        return longest
        # for i in range(len(sortedNums)):
        #     for j in range(i, len(sortedNums)):
        #         if (sortedNums[j] not in seq):
        #             if (j - 1 >= 0 and sortedNums[j-1] == sortedNums[j] - 1):
        #                 seq.add(sortedNums[j])
        #                 longest = max(longest, len(seq))
        #             else:
        #                 break;
                    






