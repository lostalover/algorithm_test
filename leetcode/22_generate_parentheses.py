from typing import List


class Solution:
    result = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.__add_match("", n, n)
        return self.result

    def __add_match(self, cur=str, l=int, r=int):
        if l < r or l < 0 or r < 0:
            return
        if l == 0 and r == 0:
            self.result.append(cur)

        l_cur = cur + ")"
        self.__add_match(l_cur, l-1, r)
        r_cur = cur + "("
        self.__add_match(r_cur, l, r-1)


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
