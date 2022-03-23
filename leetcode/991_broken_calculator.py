class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        result = 0
        value = target
        while True:
            if startValue < value and value % 2 == 0:
                value = value // 2
            elif startValue < value:
                value = value + 1
            else:
                break
            result += 1
        temp = startValue - value
        return result + temp


print(Solution().brokenCalc(2, 3))
print(Solution().brokenCalc(5, 8))
print(Solution().brokenCalc(3, 10))
