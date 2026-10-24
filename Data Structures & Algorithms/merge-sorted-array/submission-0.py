class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = len(nums1) - 1
        j = len(nums2) - 1;
        i = m - 1
        while last >= 0:
            print(f"i:{i}, j:{j} last:{last}")
            if (i >= 0 and j >= 0 and nums1[i] > nums2[j]):
                nums1[last], nums1[i] = nums1[i], nums1[last]
                i -= 1
                last -= 1
            elif (j >= 0 and i >= 0 and nums1[i] < nums2[j]):
                nums1[last], nums2[j] = nums2[j], nums1[last]
                # nums2[j] = -99
                j -= 1
                last -= 1
            else:
                print("DONE")
                # When i or j is -1 already aka we only compare against if j is not all taken yet or i (0 case)
                while j >= 0:
                    print(f"i:{i}, j:{j} last:{last}")
                    nums1[last] = nums2[j]
                    j -= 1
                    last -= 1
                while i >= 0:
                    print(f"i:{i}, j:{j} last:{last}")
                    nums1[last] = nums1[i]
                    i -= 1
                    last -= 1

                
            print(nums1)
            
            # last -= 1
        

    
            


