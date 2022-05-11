# failed searching starting point
from typing import List


class CircularArray:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.arr_length = len(arr)

    def get_data(self, n):
        n = n % self.arr_length
        return self.arr[n]


def binary_search(arr: CircularArray, target, low=None, high=None):
    low, high = low or 0, high or arr.arr_length - 1
    if low > high:
        return None
    mid = (low + high) // 2
    mid_val = arr.get_data(mid)
    if low == high and mid_val != target:
        return None
    if mid_val > target:
        return binary_search(arr, target, low, mid)
    if mid_val == target:
        return mid
    if mid_val < target:
        return binary_search(arr, target, mid + 1, high)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_pos = self.__find_start_pos(nums)
        arr = CircularArray(nums)
        target = binary_search(arr, target, start_pos, start_pos + len(nums) - 1)
        return target if target is not None else -1

    def __find_start_pos(self, nums, low=None, high=None):
        low, high = low or 0, high or len(nums) - 1
        mid = (low + high) // 2
        low_val = nums[low]
        mid_val = nums[mid]
        high_val = nums[high]
        if nums[mid] > nums[low] and nums[mid] > nums[high]:
            return self.__find_start_pos(nums, mid+1, high)
        elif nums[mid] < nums[low] and nums[mid] < nums[high]:
            return self.__find_start_pos(nums, low, mid)
        elif nums[low] < nums[(low-1)%len(nums)]:
            return low
        elif nums[high] > nums[(high+1)%len(nums)]:
            return high + 1
        else:
            return 0

# Solution().search(nums = [4,5,6,7,0,1,2], target = 3)
# Solution().search(nums = [1], target = 0)
Solution().search(nums = [5,6,7,0,1,2,4], target = 0)
