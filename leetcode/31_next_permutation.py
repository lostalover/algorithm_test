from typing import List


class Solution:
    def __swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_idx = len(nums) - 1
        if nums[max_idx] > nums[max_idx-1]:
            self.__swap(nums, max_idx, max_idx-1)
            return nums
        else:
            compare_idx = max_idx-1
            while compare_idx >= 0:
                if nums[compare_idx] < nums[compare_idx+1]:
                    diff = 101
                    change_idx = int
                    for i in range(compare_idx+1, max_idx+1):
                        if nums[compare_idx] < nums[i] and nums[i] - nums[compare_idx] <= diff:
                            change_idx = i
                            diff = nums[i] - nums[compare_idx]
                    self.__swap(nums, compare_idx, change_idx)
                    nums[compare_idx+1:] = reversed(nums[compare_idx+1:])
                    return nums
                compare_idx -= 1
            nums[:] = reversed(nums[:])
            return nums


# print(Solution().nextPermutation([1, 2, 3]))
# print(Solution().nextPermutation([3, 2, 1]))
# print(Solution().nextPermutation([1, 3, 2]))
# print(Solution().nextPermutation([1, 1, 5]))
# print(Solution().nextPermutation([1,6,9,5,4,2,1]))
print(Solution().nextPermutation([2, 3, 1, 3, 3]))
