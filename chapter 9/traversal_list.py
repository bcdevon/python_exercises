# list_a = [1, 3, 4, 6, 7]
# list_b = [1, 3, 4, 6, 7]
# list_c = [1, 4, 5, 7, 8]
# list_d = [2, 9, 5, 13, 6, 10, 3]
# if list_a == list_c:
#     print("true")
# else: 
#     print("False")
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

def inorder_traversal(root):
    list = []
    if root is not None:
        inorder_traversal(root.left)
        list.append(root.val)
        inorder_traversal(root.right)
    return list
  

# if inorder_traversal(root) == list_d:
#     print("True")
# else:
#     print("False")

