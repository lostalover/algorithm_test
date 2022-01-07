class Solution:
    def reverse(self, x: int) -> int:
        if x < -(2**31) or x > 2**31-1:
            return 0
        negative = False
        if x < 0:
            negative = True
        x = -x if negative else x
        str_x = str(x)
        reverse_x = str_x[::-1]
        result = int(reverse_x)*-1 if negative else int(reverse_x)
        if result < -(2**31) or result > 2**31-1:
            return 0
        else:
            return result
