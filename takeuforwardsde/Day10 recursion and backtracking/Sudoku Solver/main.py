class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        alls = set([str(x) for x in range(1, 10)])
        memoBoard = prepareMemoBoard(board)
        solve(board, 0, 0, memoBoard, alls)


def prepareMemoBoard(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    box = [[set() for _ in range(3)] for _ in range(3)]
    for y in range(9):
        for x in range(9):
            val = board[y][x]
            rows[y].add(val)
            cols[x].add(val)
            box[y // 3][x // 3].add(val)
    return rows, cols, box


def getCandidates(board, y, x, memoBoard, alls):
    rows, cols, box = memoBoard
    return alls.difference(rows[y]).difference(cols[x]).difference(box[y // 3][x // 3])


def solve(board, y, x, memoBoard, alls):
    if y == 9:
        return True
    else:
        ynext, xnext = (y + (x + 1) // 9, (x + 1) % 9)
    if board[y][x] != ".":
        return solve(board, ynext, xnext, memoBoard, alls)
    else:
        candidates = getCandidates(board, y, x, memoBoard, alls)
        row, col, box = memoBoard
        for val in candidates:
            row[y].add(val)
            col[x].add(val)
            box[y // 3][x // 3].add(val)
            isSolved = solve(board, ynext, xnext, (row, col, box), alls)
            if isSolved:
                board[y][x] = val
                return True
            else:
                row[y].remove(val)
                col[x].remove(val)
                box[y // 3][x // 3].remove(val)
        board[y][x] = "."
        return False
