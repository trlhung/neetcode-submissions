class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i: set() for i in range(9)}
        col = {i: set() for i in range(9)}
        box = {i: set() for i in range(9)}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                char = board[r][c]

                if char in row[r] or char in col[c]:
                    return False
                
                boxIdx = (r // 3) * 3 + (c // 3)

                if char in box[boxIdx]:
                    return False
                
                row[r].add(char)
                col[c].add(char)
                box[boxIdx].add(char)

        return True