from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        queue.append((0,0,1))

        if (grid[0][0] == 1):
            return -1

        destination = (len(grid) -1, len(grid[0])-1)

        grid[0][0] = 1

        while queue:
            for i in range(len(queue)):
                row,col,dist = queue.popleft()
                print(f"{row},{col}")
                if ((row,col) == destination):
                    return dist


                neighbors = [[row + 1, col], [row - 1, col], [row, col -1], [row, col +1], [row + 1, col +1], [row - 1, col -1], [row + 1, col - 1], [row - 1, col + 1]]
                for r,c in neighbors:
                    inBounds = r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

                    if (inBounds):
                        print(f"{r},{c}")
                        if (grid[r][c] == 0):
                            d = dist + 1
                            grid[r][c] = None
                            queue.append((r,c,d))

        return -1
                

