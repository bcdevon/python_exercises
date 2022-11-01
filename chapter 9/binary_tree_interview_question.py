"""This module is used to check if two binary trees are identical in both shape and value"""

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

def compare_tree_inorder(root, root_b):
    stack = []
    stack_b = []
    iter = root
    iter_b = root_b

    while (iter is not None or len(stack) > 0) and (iter_b is not None or len(stack_b) > 0):
        while iter is not None and iter_b is not None:
            stack.append(iter)
            iter = iter.left
            stack_b.append(iter_b)
            iter_b = iter_b.left
            if (iter is None and iter_b is not None) and (iter is not None and iter_b is None):
                return False
        iter = stack.pop()
        iter_b = stack_b.pop()
        if iter.val != iter_b.val:
            return False
        iter = iter.right
        iter_b = iter_b.right
        if (iter is None and iter_b is not None) and (iter is not None and iter_b is None):
                return False


    return True


'''One tree empty
trees different shape
trees different values
trees have same shape and values
check if shape of sub tree is the same
'''
