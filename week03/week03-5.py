# week03-5.py 學習計畫 Sliding Window
# LeetCode 1493. Longest Subarray of 1's After Deleting One Element
# 陣列裡, 一定要刪掉 1 個, 問剩下的陣列裡, 最長的 1 有幾個?
# Sliding Window 伸縮自如的毛毛蟲, 可容忍最多 1 個 0
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums) # 陣列的長度
        zeros = 0 # 毛毛蟲的體內, 有幾個「有毒的 0」
        tail = 0 # 毛毛蟲的尾巴, 一開始停在 0 的地方, 拉肚子時, 會往右縮
        ans = 0 # 毛毛蟲的最長的長度
        for head in range(N): # 毛毛蟲的頭頭, 逐一往右吃
            if nums[head]==0: zeros += 1 # 如果吃到「有毒的 0」zeros減1
            while zeros>1: # 有毒的0 , 太多了
                if nums[tail] == 0: zeros -= 1 # 尾巴拉便便「有毒 0」出來
                tail += 1 # 尾巴吐掉之後, 右縮
            ans = max(ans, head - tail + 1) # 更新毛毛蟲的最大長度
        return ans-1 # 題目說: 一定要刪掉一個元素
