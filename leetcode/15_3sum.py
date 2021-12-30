from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

        result = set(tuple(i) for i in result)
        result = [list(i) for i in result]
        return list(result)


if __name__ == "__main__":
    # print(len(l))
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    # print(Solution().threeSum([-14,-10,-1,8,-8,-7,-3,-2,14,10,3,3,-1,-15,6,9,-1,6,-2,-6,-8,-15,8,-3,-14,5,-1,-12,-10,-5,-9,-8,1,-3,-15,0,-3,-11,6,-11,7,-6,7,-9,-6,-10,7,1,11,-10,10,-12,-10,3,-7,-9,-7,7,-14,-9,10,14,-2,-4,-4,-10,3,1,-14,-6,5,8,-4,-11,14,-3,-6,-2,13,13,3,0,-14,8,10,-14,6,11,1,7,-13,-4,6,0,-1,10,-3,-13,-4,-2,-11,8,-8]))
    print(Solution().threeSum([0]))
