class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        countIslands = 0

        def dfs(coord):
            if (grid[coord[0]][coord[1]]) == "0":
                return

            row = coord[0]
            col = coord[1]
            if (grid[row][col]) == "1":
                grid[row][col] = "0"
            directions = [[row,col + 1],[row + 1,col],[row, col-1], [row -1, col]]
            for r,c in directions:
                if (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])):
                    print(f"check {coord[0]},{coord[1]}")
                    if (grid[r][c] == "1"):
                        dfs((r,c))

            


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    print(f"HI coord {r},{c}")
                    dfs((r,c))
                    print("HI")
                    countIslands += 1
        
        return countIslands

        

