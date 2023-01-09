"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res, stack = [], [root]
    while stack:
        n = stack.pop()
        if n:
            res.append(n.val)
            stack.append(n.right)
            stack.append(n.left)
    return res
