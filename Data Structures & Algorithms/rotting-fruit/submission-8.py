from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def returnRottenFruit():
            rotten = []
            freshFruit = []
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 2:
                        rotten.append((r, c))
                    elif grid[r][c] == 1:
                        freshFruit.append((r, c))
            return rotten, freshFruit

        queue = deque()

        fruits = returnRottenFruit()

        for i in fruits[0]:
            queue.append(i)

        if (not fruits[1]):
            return 0

        if (not fruits[0]):
            return -1
        
    

        level = -1
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for r,c in neighbors:
                    if (r > len(grid)-1 or c > len(grid[0]) - 1 or r < 0 or c < 0 or grid[r][c] == 2):
                         continue
                    
                    if (grid[r][c] == 0):
                        continue

                    print(f"{r},{c}")
                    if (grid[r][c] == 1):
                        grid[r][c] = 2
                        queue.append((r,c))
            level += 1    

        for r,c in fruits[1]:
            if (grid[r][c] == 1):
                return -1

        return level