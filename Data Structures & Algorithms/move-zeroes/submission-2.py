class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0

        for i in range(j + 1, len(nums)):
            print(nums)
            print(f"i:{i}, j:{j}")
            if nums[i] == 0:
                if (nums[j] != 0):
                    j += 1
                continue

            if (nums[j] != 0):
                j += 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            

        