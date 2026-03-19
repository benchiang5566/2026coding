# week04-4a.py 學習計畫 Prefix Sum 第一題
# week04-4a.py 是改寫 week04-2.py
# LeetCode 1732. Find the Highest Altitude
# 找到最高的海拔高度 (一直加, 就對了 !)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0 # 一開始的高度是 0
        for gg in gain: # Python 進階 for 迴圈: 依序取處 gg, 從 gian 中
            H += gg
            ans = max(ans, H)
        return ans
