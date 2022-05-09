class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        center = 0
        seen = {}
        result = []
        for i, ch in enumerate(s):
            if ch in seen:
                if ch == s[i-1]:
                    pass
                elif ch == s[i-2]:
                    pass
            else:
                seen[ch] = i
                end += 1
        return result

Solution().longestPalindrome("cbbd")