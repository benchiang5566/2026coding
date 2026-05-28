# week14-3b.py 學習計畫 DP - 1D 第2題
# LeetCode 746. Min Cost Climbing Stairs
# 踩在第i格的梯子上, 要付出 cost[i] 的代價, 每次可跨1格或跨2格
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        a = [0] * (N+1) # 存答案, 建表格
        a[0] = cost[0]
        a[1] = cost[1] # 題目規格是「一定有2格」
        for i in range(2, N+1):
            a[i] = min(a[i-1], a[i-2]) # 取最小的花費
            if i < N: a[i] += cost[i]
        return a[N] # 爬完囉~~