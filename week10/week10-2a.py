```python
# week10-2a.py 學習計畫 Binary Tree - DFS
# DFS 深度優先 tree 最喜歡使用「函式呼叫函式」來解
# LeetCode 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root == None: return 0 # 沒有東西, 深度是 0
            left = helper(root.left) # 左邊的深度
            right = helper(root.right) # 左邊的深度
            return max(left, right) +
        return helper(root)
```
