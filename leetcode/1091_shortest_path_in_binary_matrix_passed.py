from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        visited = set()
        
        step = 1
        queue = [(0,0)]
        visited.add((0,0))

        while len(queue) > 0:
            for i in range(len(queue)):
                cur_r, cur_c = queue.pop(0)
                # print(cur_r, cur_c, step)
                if cur_r == n-1 and cur_c == n-1:
                    return step
                
                for r_offset in [-1,0,1]:
                    for c_offset in [-1,0,1]:
                        next_r = cur_r + r_offset
                        next_c = cur_c + c_offset

                        cond = (0 > next_r or next_r >= n \
                            or 0 > next_c or next_c >= n \
                            or grid[next_r][next_c] == 1 \
                            or (next_r, next_c) in visited)
                        if cond:
                            continue
                        
                        visited.add((next_r, next_c))
                        queue.append((next_r, next_c))
            step += 1
                                    
        return -1