class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        MARK = float('inf')  # Temporary marker

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # Mark the row
                    for c in range(cols):
                        if matrix[i][c] != 0:
                            matrix[i][c] = MARK

                    # Mark the column
                    for r in range(rows):
                        if matrix[r][j] != 0:
                            matrix[r][j] = MARK

        # Convert all markers to 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == MARK:
                    matrix[i][j] = 0