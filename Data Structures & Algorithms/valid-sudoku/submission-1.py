class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boardSq = [set() for i in range(9)]


        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                if (board[r][c] in rows[r]):
                    return False
                
                if (board[r][c] in cols[c]):
                    return False
                    

                boxIndex = (r // 3) * 3 +(c // 3);
                if board[r][c] in boardSq[boxIndex]:
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boardSq[boxIndex].add(board[r][c])
        return True



