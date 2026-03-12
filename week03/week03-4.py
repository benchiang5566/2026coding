# week03-4.py 學習計畫 Sliding Window 第3題
# LeetCode 1004. Max Consecutive Ones III
# 你可以把 k 個 0 翻轉變成 1, 那最長的一堆 1, 有幾個 1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0 # 一開始的毛毛蟲, 肚子裡沒有 0
        N = len(nums) # 陣列的長度 N
        ans = 0
        tail = 0 # 尾巴一開始棉在 0 的位置, 指有拉肚子時, 才會往右縮
        for head in range(N): # 毛毛蟲的頭頭, 慢慢往右吃
            if nums[head]==0: # 吃到 1 個「有毒的 0」
                zeros += 1 # 身體內的毒素增加
                #if zeros > k : # 超過身體可以容忍的上限, 要拉肚子!!!
                while zeros > k: # 要用 while 迴圈, 一直拉肚子/排出 0
                    if nums[tail]==0: # 現在尾巴吐掉的是 「有毒的 0」
                        zeros -= 1 # 毒素減少
                    tail += 1 # 尾巴拉肚子、拉玩後, 不能留在髒髒的原地,  往右縮
            # 排完毒完畢, 身體內保證不會有太多「有毒的 0」
            ans = max(ans, head - tail + 1) # 更新答案
        return ans  # 最長的、不會中毒而死的毛毛蟲, 長度是 ans

