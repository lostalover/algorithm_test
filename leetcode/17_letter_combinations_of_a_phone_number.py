from typing import List


class Solution:
    LUT = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        self.__save_result(digits, "")
        return self.result
    
    def __save_result(self, digits: str, created_string: str):
        if len(digits) == 0:
            return
        elif len(digits) == 1:
            s = self.LUT[digits[0]]
            for ch in s:
                self.result.append(created_string + ch)
            return
        
        print(digits[0])
        s = self.LUT[digits[0]]
        for ch in s:
            self.__save_result(digits[1:], created_string + ch)

Solution().letterCombinations("2")
Solution().letterCombinations("23")
Solution().letterCombinations("")