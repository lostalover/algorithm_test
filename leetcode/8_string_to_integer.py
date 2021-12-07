class Solution:
    is_n = False
    MIN = -(2**31)
    MAX = (2**31) - 1

    def __step_one(self, s: str) -> str:
        for i in range(0, len(s)):
            if s[i] == " ":
                continue
            else:
                return s[i:]
        return ""

    def __step_two(self, s: str) -> str:
        if len(s) == 0:
            return s

        if s[0] == '-':
            self.is_n = True
            return s[1:]
        elif s[0] == '+':
            return s[1:]
        else:
            return s

    def __step_three(self, s: str) -> str:
        for i in range(0, len(s)):
            if s[i].isdigit():
                continue
            else:
                return s[0:i]
        return s

    def __step_four(self, s: str) -> str:
        if len(s) == 0:
            return 0
        else:
            return int(s)

    def __step_five(self, s: int) -> str:
        s = s if self.is_n is False else -s
        if s <= self.MIN:
            s = self.MIN
        elif s >= self.MAX:
            s = self.MAX
        return s

    def myAtoi(self, s: str) -> int:
        s = self.__step_one(s)
        s = self.__step_two(s)
        s = self.__step_three(s)
        s = self.__step_four(s)
        s = self.__step_five(s)
        return s


# if __name__ == "__main__":
#     print(Solution().myAtoi("  42"))
#     print(Solution().myAtoi("   -42"))
#     print(Solution().myAtoi("  4193 with words"))
#     print(Solution().myAtoi("  words and 987"))
#     print(Solution().myAtoi("  -91283472332"))