"""
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack, cur = [], ''
        for c in s:
            if c == '(':
                stack += [cur]
                cur = ''
            elif c == ')':
                if stack:
                    cur = stack.pop() + '(' + cur + ')'
            else:
                cur += c

        while stack:
            cur = stack.pop() + cur

        return cur