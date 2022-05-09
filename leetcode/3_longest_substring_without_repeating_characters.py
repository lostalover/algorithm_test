class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        count = 1
        seen = {}
        for i, ch in enumerate(s):
            while True:
                if ch in seen:
                    del seen[s[start]]
                    start += 1
                else:
                    seen[ch] = i
                    potential_max = end - start + 1
                    if potential_max > count:
                        count = potential_max
                    end += 1
                    break
        return count

print(Solution().lengthOfLongestSubstring("abcabcbb"))