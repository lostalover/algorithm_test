from typing import List


class Solution:
    def initialize(self, board, word) -> None:
        self.board = board
        self.height = len(board)
        self.length = len(board[0])
        self.visited = [[False]*self.length for i in range(self.height)]
        self.word = word

    def dfs(self, cur_i, cur_j, cur_word_idx):
        if cur_word_idx == len(self.word):
            return True
        if cur_i < 0 or cur_i >= self.height:
            return False
        if cur_j < 0 or cur_j >= self.length:
            return False
        cur_ch = self.board[cur_i][cur_j]
        print(f'{cur_i} {cur_j} {cur_ch} checking if I am on {self.word[cur_word_idx]}')
        if self.visited[cur_i][cur_j] is False:
            self.visited[cur_i][cur_j] = True
            if cur_ch == self.word[cur_word_idx]:
                cur_word_idx += 1
                if self.dfs(cur_i, cur_j + 1, cur_word_idx):
                    return True
                if self.dfs(cur_i, cur_j - 1, cur_word_idx):
                    return True
                if self.dfs(cur_i + 1, cur_j, cur_word_idx):
                    return True
                if self.dfs(cur_i - 1, cur_j, cur_word_idx):
                    return True
                cur_word_idx -= 1
            self.visited[cur_i][cur_j] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.initialize(board, word)
        for i in range(self.height):
            for j in range(self.length):
                if word[0] == board[i][j]:
                    self.visited = [[False]*self.length for i in range(self.height)]
                    if self.dfs(i, j, 0):
                        return True
        return False


# print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
# print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
# print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
