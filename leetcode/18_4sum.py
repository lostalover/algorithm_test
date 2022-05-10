from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        result_set = set()
        dictionary = {}
        for i, num in enumerate(nums):
            if num in dictionary:
                dictionary[num].add(i)
            else:
                dictionary[num] = set([i])
        
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    remain = target - (nums[i] + nums[j] + nums[k])
                    if remain in dictionary:
                        if len(dictionary[remain] - set([i, j, k])) != 0:
                            temp_list = [nums[i], nums[j], nums[k], remain]
                            temp_list.sort()
                            result_set.add((temp_list[0], temp_list[1], temp_list[2], temp_list[3]))

        for data in result_set:
            result.append(list(data))
        return result

# Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0)
Solution().fourSum(nums = [1], target = 0)