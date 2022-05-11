# Time Limit Exceed
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = not (self.__is_positive(dividend)^self.__is_positive(divisor))
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 1 if dividend == divisor else 0
        
        while dividend > divisor:
            dividend -= divisor
            result += 1

        return result if positive else -result
    
    def __is_positive(self, n: int):
        return True if n >= 0 else False

# Solution().divide(10, 3)
Solution().divide(1, 1)
