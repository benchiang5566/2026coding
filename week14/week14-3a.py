# week14-3a.py 學習計畫 DP - 1D 第2題
# LeetCode 746. Min Cost Climbing Stairs
# 踩在第i格的梯子上, 要付出 cost[i] 的代價, 每次可跨1格或跨2格
# from functools import * 平常要使用 @cache 要記得呼叫套件 
from functools import *
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache # 函式呼叫函式
        def helper(i): # 現在踩在第i格, 之後要多少錢
            if i>=len(cost): return 0 # 走完了
            return cost[i] + min(helper(i+1), helper(i+2)) # 一定要錢, 我們是先知選最小的
        return min(helper(0), helper(1)) # 跨1步, 還是跨2步, 選最小的