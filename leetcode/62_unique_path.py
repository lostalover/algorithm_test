class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        arr = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    arr[0][0] = 0
                elif i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i][j-1] + arr[i-1][j]
        return arr[m-1][n-1]

print(Solution().uniquePaths(1, 1))