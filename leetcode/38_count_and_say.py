class Solution:
    def __say(self, s: str):
        result = ""
        count = 1
        if len(s) == 1:
            result += '1' + s
        for i in range(1, len(s)):
            prev = s[i-1]
            if prev == s[i]:
                count += 1
            else:
                result += str(count) + prev
                count = 1
            if i == len(s)-1:
                result += str(count) + s[i]
        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.__say(self.countAndSay(n-1))

# print(Solution().countAndSay(1))
# print(Solution().countAndSay(2))
# print(Solution().countAndSay(3))
print(Solution().countAndSay(4))
