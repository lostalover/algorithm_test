from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.n = n
        result = [[0] * n for i in range(n)]
        self.visited = [[False] * n for i in range(n)]
        direction = [[0,1], [1,0], [0,-1], [-1,0]]

        cur_dir = 0
        cur_cordinate = [0,0]
        result[0][0] = 1
        val = 2
        self.visited[0][0] = True
        while True:
            next_cordinate = [cur_cordinate[0] + direction[cur_dir][0], cur_cordinate[1] + direction[cur_dir][1]]
            if self.__should_be_rotated(next_cordinate) == True:
                if self.__is_end(cur_cordinate, direction) == True:
                    return result
                cur_dir = (cur_dir + 1) % len(direction)
                continue
            result[next_cordinate[0]][next_cordinate[1]] = val
            self.visited[next_cordinate[0]][next_cordinate[1]] = True
            cur_cordinate = next_cordinate
            val += 1

    def __should_be_rotated(self, next_cordinate):
        cond = (next_cordinate[0] >= self.n or next_cordinate[0] < 0) \
            or (next_cordinate[1] >= self.n or next_cordinate[1] < 0)
        if cond:
            return True
        if self.visited[next_cordinate[0]][next_cordinate[1]]:
            return True
        return False

    def __is_end(self, cur_cordinate, direction):
        for i, val in enumerate(direction):
            pos = [cur_cordinate[0] + val[0], cur_cordinate[1] + val[1]]
            if self.__should_be_rotated(pos) == False:
                return False
        return True

Solution().generateMatrix(3)
