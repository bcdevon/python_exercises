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

root_a = TreeNode(31)
root_a.left = TreeNode(15)
root_a.right = TreeNode(120)
root_a.left.left = TreeNode(21)
root_a.left.right = TreeNode(39)
root_a.right.left = TreeNode(13)
root_a.right.right = TreeNode(6)

root_b = TreeNode(3)
root_b.left = TreeNode(5)
root_b.right = TreeNode(10)
root_b.left.left = TreeNode(2)
root_b.left.right = TreeNode(9)
root_b.right.left = TreeNode(13)
root_b.right.right = TreeNode(6)

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
    # res = []
    # stack = []
    # cur = root
    # while cur or stack:
    #     while cur:
    #         stack.append(cur)
    #         cur = cur.left
    #     cur = stack.pop()
    #     res.append(cur.val)
    #     cur = cur.right
    # print(res)
    stack = []
    compare = []
    iter = root

    while iter is not None or len(stack) > 0:
        while iter is not None:
            stack.append(iter)
            iter = iter.left
        iter = stack.pop()
        compare.append(iter.val)
        iter = iter.right
    return compare


def compare_trees(root_a, root_b):
    stack_a = traverse_tree_inorder(root_a)
    stack_b = traverse_tree_inorder(root_b)
    if stack_a == stack_b:
        print("True")
    else:
        print("False")

compare_trees(root, root_b)