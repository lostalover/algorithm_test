from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_row = [False for _ in range(rows)]
        zero_col = [False for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_row[i] = True
                    zero_col[j] = True

        for i in range(rows):
            for j in range(cols):
                if zero_row[i] == True \
                        or zero_col[j] == True:
                    matrix[i][j] = 0
