from functools import cache

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        @cache
        def build(start: int, end: int) -> list[TreeNode | None]:
            if start > end:
                return [None]

            trees = []
            for root_val in range(start, end + 1):
                left_subtrees = build(start, root_val - 1)
                right_subtrees = build(root_val + 1, end)

                for left in left_subtrees:
                    for right in right_subtrees:
                        trees.append(TreeNode(root_val, left, right))

            return trees

        return build(1, n)