class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowSet = [set() for i in range(9)]
        colSet = [set() for i in range(9)]
        boardSet = [set() for i in range(9)]

        # Check rows
        for row in range(9):
            for col in range(9):
                num = board[row][col];

                if (num == '.'):
                    continue

                boardVal = (row // 3) * 3 + (col // 3)
                
                if num in rowSet[row]:
                    return False
                if num in colSet[col]:
                    return False
                if num in boardSet[boardVal]:
                    return False

                rowSet[row].add(num)
                colSet[col].add(num)
                boardSet[boardVal].add(num)

        return True

