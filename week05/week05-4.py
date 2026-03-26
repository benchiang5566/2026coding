## week05-4.py 昨天 2026-03-25 的挑戰題
## LeetCode 3546. Equal Sum Grid Partition I
## grid 矩陣，能否「切一刀」兩邊和「剛好相同」
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum([sum(row) for row in grid]) ## 先把 total 算出來

        preSum = 0 ## 利用 prefix sum 技巧「由上到下」逐 row 相加, 對應橫切一刀
        for row in grid: ## grid 裡，每個 row 逐一處裡
            preSum += sum(row) ## 加入 preSum 變數
            if total - preSum == preSum: ## 如果「下半==上半」
                return True ## 就成功「切一半」

        preSum = 0 ## 利用 prefix sum 技巧「左到右」逐 col 相加
        for col in zip(*grid): ## 把 transpose 轉置矩陣, 逐個處裡
            preSum += sum(col) ## grid 裡，每個 col 逐一加到 preSum 裡
            if total - preSum == preSum: ## 如果「右半==左半」
                return True ## 就成功「切一半」
        return False ## 如果「所有的切法」都沒成功，就失敗
