'''
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
'''

class Solution(object):
    def maxDepth(self, s):
        result = count = 0
        for i in s:
            if i == '(':
                count += 1
            if i == ')':
                result = max(result, count)
                count -= 1
        return result