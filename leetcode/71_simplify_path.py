class Solution:
    def simplifyPath(self, path: str) -> str:
        import os
        return os.path.abspath(os.path.expanduser(path))


print(Solution().simplifyPath("/home/"))
print(Solution().simplifyPath("/../"))
print(Solution().simplifyPath("/home//foo/"))
