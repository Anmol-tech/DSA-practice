'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.find_diameter(root)
        return self.diameter

    def find_diameter(self, root):
        if root.left is None and root.right is None:
            return 1

        left = self.find_diameter(root.left) if root.left is not None else 0
        right = self.find_diameter(root.right) if root.right is not None else 0
        self.diameter = max(self.diameter, left + right)
        return max(left, right) + 1



