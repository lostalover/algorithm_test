from typing import List


class Solution:
    def __binary_search(self, arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.__binary_search(arr, low, mid - 1, x)
            else:
                return self.__binary_search(arr, mid + 1, high, x)
        else:
            return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            for data in row:
                arr.append(data)
        result = self.__binary_search(arr, 0, len(arr)-1, target)
        result = True if result != -1 else False
        return result


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20],
                               [23, 30, 34, 60]], 13))
