# week11-4.py 學習計畫 第 2 題
# LeetCode 450. Delete Node in a BST
# 把某個 node 殺掉, 在找到繼承者, 放在格子裡
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def fascist(root): # 找到極右 findRighrtest
            if root.right: # 右邊還有繼續找
                return fascist(root.right)
            return root # 沒有右邊, 就是本身的點上

        if root==None: return root
        if root.val==key:
            if root.left:
                now = fascist(root.left) # 找到繼承者 now
                root.val = now.val # 把繼承者的值「替代掉」
                root.left = self.deleteNode(root.left, now.val) # 再把左邊小樹裡面原繼承者的位置刪掉
                return root # 結束
            #root.val = 999 debug 用
            else:
                return root.right

        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
