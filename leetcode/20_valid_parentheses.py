class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        self.LUT = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for i, val in enumerate(s):
            open_cond = val == '(' \
                or val == '{' \
                or val == '['
            if open_cond:
                self.stack.append(val)
            else:
                if len(self.stack) > 0:
                    pop_val = self.stack.pop()
                else:
                    return False
                if val == self.LUT[pop_val]:
                    pass
                else:
                    return False
        return True if len(self.stack) == 0 else False

Solution().isValid("()")

