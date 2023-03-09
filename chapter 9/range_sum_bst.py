class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(11)

def rangeSumBST(root, low, high):
    total = 0
    stack = [root]

    while len(stack) > 0:
        node = stack.pop()

        if node is not None:
            if low <= node.val and high >= node.val:
                total += node.val

            # if low < node.val:
                stack.append(node.left)

            # if high > node.val:
                stack.append(node.right)
    print(total)

rangeSumBST(root, 10, 13)





