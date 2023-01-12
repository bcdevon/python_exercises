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

def rangeSumBST(root, low, high):
    total = 0
    stack = [root]

    while len(stack) > 0:
        node = stack.pop()

        if node is not None:
            if low <= node.val and high >= node.val:
                total += node.val

            if low < node.val:
                stack.append(node.left)

            if high > node.val:
                stack.append(node.right)
    return total

print(rangeSumBST(root, 2, 10))
