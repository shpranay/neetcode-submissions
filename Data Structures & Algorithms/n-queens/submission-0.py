class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def solve(row, board):
            if row == n:
                result.append(board[:])
                return

            for col in range(n):
                # Check column
                if any(board[i][col] == 'Q' for i in range(row)):
                    continue

                # Check left diagonal
                if any(
                    col - row + i >= 0 and board[i][col - row + i] == 'Q'
                    for i in range(row)
                ):
                    continue

                # Check right diagonal
                if any(
                    col + row - i < n and board[i][col + row - i] == 'Q'
                    for i in range(row)
                ):
                    continue

                # Place queen
                new_board = board[:]
                new_board[row] = '.' * col + 'Q' + '.' * (n - col - 1)

                solve(row + 1, new_board)

        solve(0, ['.' * n for _ in range(n)])
        return result