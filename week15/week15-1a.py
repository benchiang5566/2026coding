# week15-1a.py 學習計畫 DP - Multidimensional 第1題
# LeetCode 62. Unique Paths
from functools import *
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache # 函式呼叫函式
        def helper(i,j): # 現在若在 (i,j) 座標
            if i==m-1 and j==n-1: return 1 # 走到終點, 成功記 1
            if i==m or j==n: return 0 # 撞到牆了, 失敗記 0
            return helper(i+1, j) + helper(i, j+1)
        return helper(0, 0) # 記得呼叫