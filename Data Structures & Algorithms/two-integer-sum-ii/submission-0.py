class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = 0
        for i in range(len(numbers)-1, -1, -1):
            print(f"{j}, {i}")
            while target > numbers[j] + numbers[i]:
                j += 1
            if numbers[i] + numbers[j] == target:
                return [j+1, i+1]

        return []