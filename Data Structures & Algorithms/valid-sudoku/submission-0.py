class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        squares = []

        for i in range(9):
            rows.append(set())
            cols.append(set())
            squares.append(set())

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                
                if curr not in rows[i]:
                    rows[i].add(curr)
                else:
                    return False

                if curr not in cols[j]:
                    cols[j].add(curr)
                else:
                    return False
                
                index = (i // 3) * 3 + (j // 3)
                if curr not in squares[index]:
                    squares[index].add(curr)
                else:
                    return False
        return True
                