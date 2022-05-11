# failed case :
# "(()()"
# "()(()"
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        result = 0
        pop_count = 0
        complete_match_count = 0
        for i, val in enumerate(s):
            if val == '(':
                stack.append(val)
            elif val == ')':
                if len(stack) > 0:
                    result = 2
                    pop_count += 1
                    stack.pop()
                    if len(stack) == 0:
                        complete_match_count = pop_count
                        if complete_match_count*2 > result:
                            result = complete_match_count*2
                else:
                    stack = []
                    if pop_count*2 > result:
                        result = pop_count*2
                    pop_count = 0
                    complete_match_count = 0

        if len(stack) == 0:
            if pop_count*2 > result:
                result = pop_count*2
        else:
            if complete_match_count*2 > result:
                result = complete_match_count*2
        return result

# Solution().longestValidParentheses("(()")
# Solution().longestValidParentheses("")
Solution().longestValidParentheses("(()()()()(")
