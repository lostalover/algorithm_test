# Time Limit Exceeds
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        visited = [[False] * n for _ in range(n)]
        
        step = 1
        queue = [(0,0,step)]
        visited[0][0] = True

        while len(queue) > 0:
            cur_r, cur_c, step = queue.pop(0)
            print(cur_r, cur_c, step)
            if cur_r == n-1 and cur_c == n-1:
                return step

            for r_offset in [-1,0,1]:
                for c_offset in [-1,0,1]:
                    next_r = cur_r + r_offset
                    next_c = cur_c + c_offset
                    print(f'    {next_r} {next_c}')
                    cond = (0 > next_r or next_r >= n \
                        or 0 > next_c or next_c >= n \
                        or grid[next_r][next_c] == 1 \
                        or visited[next_r][next_c] == True)
                    if cond:
                        continue

                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c, step+1))
        return -1

Solution().shortestPathBinaryMatrix([[0,1],[1,0]])
