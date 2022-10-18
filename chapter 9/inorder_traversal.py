"""This module is used to inorder traverse a binary tree."""

class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
#        3
#      /   \
#    5      10
#   / \    /  \
#  2   9  13   6
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(10)
root.left.left = TreeNode(2)
root.left.right = TreeNode(9)
root.right.left = TreeNode(13)
root.right.right = TreeNode(6)

def traverse_tree_inorder(root):
    """Given the root, traverse the binary tree inorder, creating a list 
    of the nodes (or node values). 

    Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    Args:
        root:
            TreeNode. Root of the binary tree.

    Return:
        Return the intersecting list node. If there isn't one, return None.
        Examples:

            Image a tree: https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg
            return [1,3,2]
    """

    return []
