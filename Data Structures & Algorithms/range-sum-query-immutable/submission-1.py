class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        prefixRight = self.prefix[right]

        if left == 0:
            prefixLeft = 0
        else:
            prefixLeft = self.prefix[left - 1]
        return prefixRight - prefixLeft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)