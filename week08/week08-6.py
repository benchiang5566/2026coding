# week08-6.py 學習計畫 Binary Search 第4題
# LeetCode 875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 準備一個函式 helper(ans) 看答案對不對
        def helper(k): # 1 小時吃 k 香蕉, 能成功吃完嗎?
            total = 0 # 你猜k, 他會用多少時間
            for pile in piles: # 很多堆香蕉, 逐一檢查
                total += pile // k # 要吃掉這堆香蕉 piles 要花多少時間
                if pile % k > 0: total += 1 # 有餘數, 再多1小時
            return total <= h # 符合條件(在 h 小時內吃完)
        return bisect_left(range(1, max(piles)), True, key=helper) + 1
