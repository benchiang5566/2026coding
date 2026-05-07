## Definition for a binary tree node.
## class TreeNode:
##     def __init__(self, x):
##         self.val = x
##         self.left = None
##         self.right = None
## week11-2.py 學習計畫 最後一題
## LeetCode 236. Lowest Common Ancestor of a Binary Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = [] ## 負責記答案
        def helper(root):
            count = 0 ## 請問你下面累積幾個 p 或 q 的 node
            if root==None: return 0 ## 沒有東西
            if root==p or root==q: count += 1 ## 找到 1 個
            count += helper(root.left)
            count += helper(root.right)
            if count == 2: ## 收集齊 2 個
                a.append(root)
            return count ## 算完答案, 傳出結果
        helper(root) ## 記得建立函式要「呼叫使用」
        return a[0]

