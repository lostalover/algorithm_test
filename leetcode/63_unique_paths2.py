from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.n = len(obstacleGrid)
        self.m = len(obstacleGrid[0])
        result = self.__get_result(obstacleGrid)
        return result

    def __get_result(self, grid):
        dp = [[0]*self.m for _ in range(self.n)]
        visited = [[False]*self.m for _ in range(self.n)]
        self.queue = []

        cur_pos = [0,0]
        visited[cur_pos[0]][cur_pos[1]] = True
        self.queue.append(cur_pos)
        while len(self.queue) > 0:
            cur_pos = self.queue.pop(0)
            if self.__is_obstacle(cur_pos, grid):
                continue

            left_pos = [cur_pos[0], cur_pos[1] - 1]
            up_pos = [cur_pos[0] - 1, cur_pos[1]]
            right_pos = [cur_pos[0], cur_pos[1] + 1]
            down_pos = [cur_pos[0] + 1, cur_pos[1]]

            left_val = dp[left_pos[0]][left_pos[1]] if self.__is_in_bound(left_pos) is True else -1
            up_val = dp[up_pos[0]][up_pos[1]] if self.__is_in_bound(up_pos) is True else -1
            if left_val == -1 \
                    or up_val == -1:
                dp[cur_pos[0]][cur_pos[1]] = 1
            else:
                dp[cur_pos[0]][cur_pos[1]] = left_val + up_val

            self.__add_to_queue(right_pos, visited)
            self.__add_to_queue(down_pos, visited)
        
        return dp[self.n - 1][self.m - 1]

    def __is_obstacle(self, pos, grid):
        return True if grid[pos[0]][pos[1]] == 1 else False

    def __is_in_bound(self, pos):
        cond = (pos[0] >= self.n or pos[0] < 0) \
            or (pos[1] >= self.m or pos[1] < 0)
        if cond:
            return False
        else:
            return True

    def __is_not_visited(self, pos, visited):
        return True if visited[pos[0]][pos[1]] is False else False

    def __add_to_queue(self, pos, visited):
        # t1 = self.__is_in_bound(pos)
        # t2 = self.__is_not_visited(pos, visited)
        if self.__is_in_bound(pos) \
                and self.__is_not_visited(pos, visited):
            self.queue.append(pos)
            visited[pos[0]][pos[1]] = True


Solution().uniquePathsWithObstacles([[0,0,0,0],[0,1,0,0],[0,0,0,0]])
