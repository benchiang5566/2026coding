## week03-2.py 學習計畫 Sliding Windows 第1題
## LeetCode 643. Maximum Average Subarray I
## 用 Sliding Window 毛毛蟲的解法
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums) ## 陣列的長度
        total = sum( nums[:k] ) ## 加總 [:k] 前 k 項
        maxTotal = total
        for i in range(k, N): ## 右邊的頭
            total = total + nums[i] - nums[i-k]
            ## nums[i] 右邊的頭(往右吃), nums[i-k]左邊的尾, 吐出來
            maxTotal = max(maxTotal, total) ## 持續更新, 找到最大的 total
        return maxTotal / k ## 最大的平均 = 最大的 Total / k
