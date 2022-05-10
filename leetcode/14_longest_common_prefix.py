from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.result = ""
        self.strs = strs
        for i in range(len(strs[0])):
            start = 0
            end = 1 + i
            while end <= len(strs[0]):
                substring = strs[0][start:end]
                if self.__exists_in_strs(substring):
                    self.__save_result(substring)
                start += 1
                end += 1
        return self.result

    def __save_result(self, substring: str):
        if len(substring) > len(self.result):
            self.result = substring
            print(f'{self.result} {substring}')

    def __exists_in_strs(self, substring: str):
        print(substring)
        for i in range(1, len(self.strs)):
            if self.strs[i].find(substring) == -1:
                return False
        return True

# Solution().longestCommonPrefix(["flower","flow","flight"])
print(Solution().longestCommonPrefix(["reflower","flow","flight"]))