class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        firstRow = True
        firstCol = True

        # Check if first row contains 0
        for j in range(cols):
            if matrix[0][j] == 0:
                firstRow = True
                break

        # Check if first column contains 0
        for i in range(rows):
            if matrix[i][0] == 0:
                firstCol = True
                break

        # Use first row and first column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to 0 based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if firstRow:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero out first column if needed
        if firstCol:
            for i in range(rows):
                matrix[i][0] = 0