from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        self.nums = nums
        self.nums.sort()

        i = 0
        while i < len(self.nums):
            cur = self.nums[i]
            next = self.nums[i + 1] if i + 1 < len(self.nums) else None
            if cur == next:
                i = i + 3
            # elif next is None or cur != next:
            else:
                return cur

# t = Solution().singleNumber([2,2,3,2])
# print(t)
t = Solution().singleNumber([0,1,0,1,0,1,99])
print(t)
