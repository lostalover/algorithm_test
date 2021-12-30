from typing import List


RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
HEADING = [[0, 1], [1, 0], [0, -1], [-1, 0]]


class Solution:
    def __initialize(self, matrix: List[List[int]]) -> None:
        self.size_heigh = len(matrix[0])
        self.size_length = len(matrix)
        self.result = []
        self.visited = [[False] * len(matrix[0]) for _ in matrix]

    def __is_visited(self, i, j):
        return self.visited[i][j]

    def __is_out_of_matrix(self, i, j):
        if i < 0 or i >= self.size_length:
            return True
        if j < 0 or j >= self.size_heigh:
            return True
        return False

    def __save_next(self, direction, i, j, matrix) -> None:
        if self.__is_out_of_matrix(i, j) or self.__is_visited(i, j):
            return
        self.visited[i][j] = True
        self.result.append(matrix[i][j])
        next_pos = [i+HEADING[direction][0], j+HEADING[direction][1]]
        if self.__is_out_of_matrix(next_pos[0], next_pos[1]) \
                or self.__is_visited(next_pos[0], next_pos[1]):
            direction = (direction + 1) % 4
            next_pos = [i+HEADING[direction][0], j+HEADING[direction][1]]
            self.__save_next(direction, next_pos[0], next_pos[1], matrix)
        else:
            self.__save_next(direction, next_pos[0], next_pos[1], matrix)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.__initialize(matrix)
        self.__save_next(0, 0, 0, matrix)
        return self.result


print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
