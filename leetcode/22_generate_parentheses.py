from typing import List


class Solution:
    result = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.__add_match("", n, n)
        return self.result

    def __add_match(self, cur=str, left=int, r=int):
        if left < r or left < 0 or r < 0:
            return
        if left == 0 and r == 0:
            self.result.append(cur)

        l_cur = cur + ")"
        self.__add_match(l_cur, left-1, r)
        r_cur = cur + "("
        self.__add_match(r_cur, left, r-1)


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
