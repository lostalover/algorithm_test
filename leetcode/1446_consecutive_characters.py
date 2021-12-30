class Solution:
    def maxPower(self, s: str) -> int:
        max_count = 0
        count = 1
        if len(s) >= 2:
            prev = s[0]
            cur = s[1]
        else:
            return 1
        for i in range(1, len(s)):
            cur = s[i]
            if cur == prev:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1
            prev = cur
        if count > max_count:
            max_count = count
            count = 1
        return max_count


if __name__ == "__main__":
    # print(Solution().maxPower("leetcode"))
    # print(Solution().maxPower("abbcccddddeeeeedcba"))
    # print(Solution().maxPower("triplepillooooow"))
    # print(Solution().maxPower("hooraaaaaaaaaaay"))
    print(Solution().maxPower("ccbccbb"))
