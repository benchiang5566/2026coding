## week11-1a.py 學習計畫 第 2 題
## LeetCode 872. Leaf-Similar Trees
## 想知道 binary tree 裡的 leaf 組出來, 是否相同
## Definition for a binary tree node.
## class TreeNode:
##     def __init__(self, val=0, left=None, right=None):
##         self.val = val
##         self.left = left
##         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = []
        def helper(root):
            if root.left == None and root.right == None:
                a.append( root.val ) ## 把值加進來 a
            if root.left: helper(root.left) ## 如果左邊有, 就往左走
            if root.right: helper(root.right) ## 如果右邊有, 就往右走
        helper(root1) ## 「函式呼叫函式」
        a, b = [], a
        helper(root2) ## 「函式呼叫函式」
        return a==b
