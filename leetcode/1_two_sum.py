from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
# class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        seen = {}
#        for i, value in enumerate(nums):
#            remaining = target - nums[i]
           
#            if remaining in seen:
#                return [i, seen[remaining]]
            
#            seen[value] = i

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))