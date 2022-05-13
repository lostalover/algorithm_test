from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        DP = [[] for i in range(501)]
        candidates.sort()
        for i in range(target + 1):
            for j in range(len(candidates)):
                diff = i - candidates[j]
                if diff > 0:
                    if len(DP[diff]) > 0:
                        for l in DP[diff]:
                            temp = [candidates[j]] + l
                            DP[i].append(temp)
                        # DP[i].append(candidates[j] + l for l in DP[diff])
                elif diff == 0:
                    DP[i].append([candidates[j]])
                else:
                    break

        # result = set()
        # for combination in DP[target]:
        #     result.add(combination)

        result = set(tuple(sorted(i)) for i in DP[target])
        result = [list(i) for i in result]
        return result

Solution().combinationSum(candidates = [2,3,6,7], target = 7)
# Solution().combinationSum(candidates = [2,7,6,3,5,1], target = 9)
