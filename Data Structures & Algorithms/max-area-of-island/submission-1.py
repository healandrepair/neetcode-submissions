class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
    

        def dfs(r, c, currTraversal):
            if grid[r][c] == 0:
                return

            if grid[r][c] == 1:
                grid[r][c] = 0

            currTraversal += [0]
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            for row, col in directions:
                if (
                    r + row >= 0
                    and r + row < len(grid)
                    and c + col >= 0
                    and c + col < len(grid[0])
                ):
                    if grid[r + row][c + col] == 1:
                        print(f"{r + row},{c + col}")
                        dfs(r + row, c + col, currTraversal)
                        print(f"currTraversal, {currTraversal}")

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    currTraversal = []
                    dfs(r, c, currTraversal)
                    print(f"curr{currTraversal}")
                    maxArea = max(maxArea, len(currTraversal))

        return maxArea

