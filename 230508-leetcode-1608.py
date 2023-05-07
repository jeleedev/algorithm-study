'''
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x
'''


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        numsLength = len(nums)
        nums.sort()

        for i in range(numsLength):
            x = numsLength - i
            if nums[i] >= x and (i == 0 or nums[i - 1] < x):
                return x
        return -1
