'''
https://leetcode.com/problems/sort-an-array/
'''
class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        merged_array = []
        L, R = 0, 0

        while L < len(left) and R < len(right):
            if left[L] < right[R]:
                merged_array.append(left[L])
                L += 1
            else:
                merged_array.append(right[R])
                R += 1
        merged_array += left[L:]
        merged_array += right[R:]

        return merged_array