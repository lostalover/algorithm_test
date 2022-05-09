class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = ["" for i in range(1001)]
        pos = 0
        is_ascending = True
        result = ""
        for i, val in enumerate(s):
            if is_ascending:
                l[pos] += val
                pos = (pos + 1) % numRows
            else:
                l[pos] += val
                pos = (pos - 1) % numRows

            if pos + 2 > numRows:
                is_ascending = False
            elif pos - 1 < 0:
                is_ascending = True
        for array in l:
            result += array
        return result


Solution().convert("PAYPALISHIRING", 3)
Solution().convert("ABC", 1)
