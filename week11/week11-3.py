## week11-3.py 學習計畫 Binary Search Tree 第 1 題
## LeetCode 700. Search in a Binary Search Tree
## Definition for a binary tree node.
## class TreeNode:
##     def __init__(self, val=0, left=None, right=None):
##         self.val = val
##         self.left = left
##         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(root, val):
            if root==None: return None ## 終止條件
            if val < root.val: ## 比較小, 走左邊
                return helper(root.left, val)
            if val > root.val: ## 比較大, 走右邊
                return helper(root.right, val)
            if val == root.val: ## 剛剛好
                return root ## 就是你
        return helper(root, val) ## 呼叫
