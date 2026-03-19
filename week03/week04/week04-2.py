# week04-2.py 學習計畫 Prefix Sum 第一題
# LeetCode 1732. Find the Highest Altitude
# 找到最高的海拔高度 (一直加, 就對了 !)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain) # 陣列的長度 N
        ans = H = 0 # 一開始的高度是 0
        # 答案一開始是 0, 因為高度一開始是 0
        for i in range(N): # 逐個加起來
            H += gain[i] # 現在的增減的量 gain[i] 加進 H
            ans = max(ans, H) # 加進最高的答案
        return ans
