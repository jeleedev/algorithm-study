'''
https://leetcode.com/problems/deepest-leaves-sum/

참고 블로그: 
https://wellsw.tistory.com/74?category=1054641
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(int)
        self.traverse(root, 1, d)

        max_depth = max(d.keys())
        return d[max_depth]

    def traverse(self, node, depth, d):
        if node is None:
            return

        d[depth] += node.val
        self.traverse(node.left, depth+1, d)
        self.traverse(node.right, depth+1, d)
