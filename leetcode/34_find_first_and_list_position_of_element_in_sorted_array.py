from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.__find_left(nums, target, 0, len(nums)-1)
        r = self.__find_right(nums, target, 0, len(nums)-1)
        return [l, r]

    def __find_left(self, nums, target, left, right):
        if len(nums) == 0:
            return -1
        mid = (left+right)//2
        while right - left > 1:
            mid = (left+right)//2
            if target <= nums[mid]:
                right = mid
            if nums[mid] < target:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return mid if nums[mid] == target else -1

    def __find_right(self, nums, target, left, right):
        if len(nums) == 0:
            return -1
        mid = (left+right)//2
        while right - left > 1:
            mid = (left+right)//2
            if target < nums[mid]:
                right = mid
            if nums[mid] <= target:
                left = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return mid if nums[mid] == target else -1

# Solution().searchRange(nums = [5,7,7,8,8,10], target = 8)
# Solution().searchRange(nums = [5,7,7,8,8,10], target = 6)
# Solution().searchRange(nums = [], target = 0)
# Solution().searchRange(nums = [1], target = 0)
# Solution().searchRange(nums = [2,2], target = 2)
# Solution().searchRange(nums = [1,4], target = 4)
Solution().searchRange(nums = [0,0,0,1,2,3], target = 0)
