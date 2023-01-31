'''
https://leetcode.com/problems/longest-palindrome/
'''
class Solution(object):
    def longestPalindrome(self, s):
        count = {}
        odd, result = 0, 0

        for char in s:
          if(char in count): continue
            
          count[char] = s.count(char)
          
          if(count[char] % 2 == 0):
              result += count[char]
          else:
              if(odd == 0): odd = 1
              result += (count[char] // 2) * 2

        return odd + result