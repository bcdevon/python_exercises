class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(10)
root.left.left = TreeNode(2)
root.left.right = TreeNode(9)
root.right.left = TreeNode(13)

root_b= TreeNode(3)
root_b.left = TreeNode(5)
root_b.right = TreeNode(10)
root_b.left.left = TreeNode(2)
root_b.left.right = TreeNode(9)
root_b.right.left = TreeNode(13)

def getTargetCopy(original, cloned, target):
    original_stack = []
    cloned_stack = []
    iter = original
    iter_b = cloned
    
    while (iter is not None or len(original_stack) > 0) and (iter_b is not None or len(cloned_stack) > 0):
        while iter is not None and iter_b is not None:
            original_stack.append(iter)
            iter = iter.left
            cloned_stack.append(iter_b)
            iter_b = iter_b.left
        iter = original_stack.pop()
        iter_b = cloned_stack.pop()
        if iter == target:
            print(iter_b.val)
        iter = iter.right
        iter_b = iter_b.right


getTargetCopy(root, root_b, root.left.left)